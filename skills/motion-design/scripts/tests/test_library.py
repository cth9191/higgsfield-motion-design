"""Behavioral checks for retrieval, provenance, portability and local video delivery."""
import copy
from http.server import ThreadingHTTPServer
import json
from pathlib import Path
import shutil
import sys
import tempfile
import threading
import unittest
import urllib.error
import urllib.request

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from library_core import ROOT, inside, load_bindings, load_library, search
from serve_library import byte_range, make_handler
from intake_study import register


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        shutil.copytree(ROOT / 'library', self.root / 'library')
        self.catalog, self.entries = load_library(self.root)

    def write_entry(self, key, change):
        entry = copy.deepcopy(self.entries[key])
        change(entry)
        (self.root / f'library/entries/{key}.json').write_text(json.dumps(entry), encoding='utf-8')

    def test_idea_and_technical_queries_retain_same_evidence(self):
        idea = search(self.catalog, 'persistent hero', video_type='product-launch')
        native = search(self.catalog, 'persistent hero', tool='Blender')
        self.assertEqual(idea[0]['id'], native[0]['id'])
        detail = self.entries[idea[0]['id']]
        self.assertEqual(detail['clip']['source_frames'], [263,438])
        self.assertTrue(detail['technical']['implementations'])
        blur = search(self.catalog, 'blur bounds', tool='After Effects')
        self.assertEqual(blur[0]['review_state'], 'rejected')
        self.assertFalse(search(self.catalog, 'blur', review_state='approved'))

    def test_video_evidence_needs_no_invented_prompt(self):
        self.assertIsNone(self.catalog['studies'][0]['original_prompt'])
        self.assertIsNone(self.catalog['studies'][0]['source_project'])

    def test_overlapping_animation_tracks_are_valid(self):
        entry = self.entries['LIGHT-INF-COPPER']
        a,b = entry['tracks'][0]['events']
        self.assertLess(b['frames'][0],a['frames'][1])
        load_library(self.root)

    def test_out_of_excerpt_event_is_rejected(self):
        self.write_entry('DETAIL-INF-DEFOCUS', lambda x:x['tracks'][0]['events'][0].update(frames=[383,430]))
        with self.assertRaisesRegex(ValueError, 'outside source excerpt'):
            load_library(self.root)

    def test_dangling_relationship_is_rejected(self):
        self.write_entry('DETAIL-INF-DEFOCUS', lambda x:x['related_ids'].append('MISSING'))
        with self.assertRaisesRegex(ValueError, 'dangling relationship'):
            load_library(self.root)

    def test_summary_cannot_silently_approve_rejected_detail(self):
        next(x for x in self.catalog['entries'] if x['id']=='DETAIL-INF-DEFOCUS')['review_state']='approved'
        (self.root/'library/catalog.json').write_text(json.dumps(self.catalog),encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'stale review index'):
            load_library(self.root)

    def test_parameters_require_basis_and_units(self):
        self.write_entry('DETAIL-INF-DEFOCUS', lambda x:x['technical']['parameters'][0].update(basis='assumed-exact'))
        with self.assertRaisesRegex(ValueError, 'provenance/units'):
            load_library(self.root)

    def test_every_shot_has_inline_technical_evidence(self):
        shots=[x for x in self.catalog['entries'] if x['kind']=='shot']
        self.assertTrue({'SHOT-INF-OPENING','SHOT-INF-QUESTION','SHOT-INF-PHONE-CARDS'}.issubset({x['id'] for x in shots}))
        for shot in shots:
            technical=self.entries[shot['id']]['technical']
            self.assertTrue(any(s.get('code') for s in technical['sections']))
            self.assertTrue(any(s.get('tables') for s in technical['sections']))
            self.assertTrue(technical['implementations'])

    def test_full_source_coverage_has_no_undocumented_frames(self):
        for study in self.catalog['studies']:
            coverage=study.get('coverage')
            if not coverage:
                continue  # Intake studies may not yet have inspected media.
            intervals=sorted(self.entries[s['id']]['clip']['source_frames'] for s in self.catalog['entries'] if s['study_id']==study['id'])
            reached=0
            for first,end in intervals:
                self.assertLessEqual(first,reached,study['id']+' has a coverage gap')
                reached=max(reached,end)
            self.assertEqual(reached,coverage['frames'],study['id'])

    def test_fractional_fps_is_supported_but_nonfinite_is_rejected(self):
        self.assertAlmostEqual(self.entries['SHOT-JAW-OPEN']['clip']['fps'],30000/1001)
        for value in [0,-1,True,float('inf'),float('nan')]:
            self.write_entry('SHOT-JAW-OPEN',lambda x:x['clip'].update(fps=value))
            with self.assertRaisesRegex(ValueError,'invalid FPS'):
                load_library(self.root)

    def test_technical_table_requires_provenance(self):
        self.write_entry('SHOT-INF-OPENING',lambda x:x['technical']['sections'][0]['tables'][0].update(basis='assumed-source'))
        with self.assertRaisesRegex(ValueError,'table provenance'):
            load_library(self.root)

    def test_technical_table_rows_match_column_labels(self):
        self.write_entry('SHOT-INF-OPENING',lambda x:x['technical']['sections'][0]['tables'][0]['rows'][0].append('unlabeled value'))
        with self.assertRaisesRegex(ValueError,'column mismatch'):
            load_library(self.root)

    def test_card_preview_must_match_opened_excerpt(self):
        self.catalog['entries'][0]['preview_asset']='infinex-defocus-preview'
        (self.root/'library/catalog.json').write_text(json.dumps(self.catalog),encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'stale preview index'):
            load_library(self.root)

    def test_portable_paths_work_and_escapes_fail(self):
        self.assertEqual(inside(self.root,'library/catalog.json'), self.root/'library/catalog.json')
        for path in ['../outside','/absolute','C:/Users/file','C:relative','library\\catalog.json']:
            with self.subTest(path=path), self.assertRaises(ValueError):
                inside(self.root,path)

    def test_unknown_binding_and_traversal_fail(self):
        manifest={'schema_version':1,'roots':{'study':str(self.root)},'bindings':{'unknown':{'root':'study','path':'file'}}}
        target=self.root/'bindings.json';target.write_text(json.dumps(manifest),encoding='utf-8')
        with self.assertRaisesRegex(ValueError,'Unknown bound asset'):
            load_bindings(target,self.catalog)
        manifest['bindings']={'infinex-reference':{'root':'study','path':'../secret'}}
        target.write_text(json.dumps(manifest),encoding='utf-8')
        with self.assertRaises(ValueError):load_bindings(target,self.catalog)

    def test_missing_local_files_do_not_break_study(self):
        self.assertEqual(load_bindings(None,self.catalog),{})
        manifest={'schema_version':1,'roots':{'study':str(self.root)},'bindings':{'infinex-reference':{'root':'study','path':'absent.mp4'}}}
        target=self.root/'bindings.json';target.write_text(json.dumps(manifest),encoding='utf-8')
        binding=load_bindings(target,self.catalog)
        self.assertFalse(binding['infinex-reference'].is_file())

    def test_intake_preserves_unknowns_and_refuses_overwrite(self):
        study=register('STUDY-NEW','A new source','https://example.com/film',root=self.root)
        catalog,entries=load_library(self.root)
        self.assertEqual(len(entries),len(self.entries))
        self.assertNotIn('coverage',study)
        self.assertIsNone(study['source_project'])
        self.assertIn('In progress',study['status'])
        before=(self.root/'library/catalog.json').read_bytes()
        with self.assertRaisesRegex(ValueError,'already exists'):
            register('STUDY-NEW','Replacement','https://example.com/other',root=self.root)
        self.assertEqual(before,(self.root/'library/catalog.json').read_bytes())


class DeliveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp=tempfile.TemporaryDirectory()
        cls.path=Path(cls.temp.name)/'sample.mp4';cls.path.write_bytes(b'0123456789abcdef')
        cls.native=Path(cls.temp.name)/'phone scene.blend';cls.native.write_bytes(b'native-test')
        handler=make_handler(bindings={'infinex-reference':cls.path,'infinex-v05-blend':cls.native})
        handler.log_message=lambda *args:None
        cls.server=ThreadingHTTPServer(('127.0.0.1',0),handler)
        cls.thread=threading.Thread(target=cls.server.serve_forever,daemon=True);cls.thread.start()
        cls.base=f'http://127.0.0.1:{cls.server.server_port}'

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown();cls.server.server_close();cls.thread.join();cls.temp.cleanup()

    def request(self,path,headers=None,method='GET'):
        return urllib.request.urlopen(urllib.request.Request(self.base+path,headers=headers or {},method=method))

    def test_seek_range_returns_correct_bytes(self):
        with self.request('/asset/infinex-reference',{'Range':'bytes=3-7'}) as response:
            self.assertEqual(response.status,206)
            self.assertEqual(response.headers['Content-Range'],'bytes 3-7/16')
            self.assertEqual(response.read(),b'34567')
        with self.request('/asset/infinex-reference',{'Range':'bytes=-4'}) as response:
            self.assertEqual(response.read(),b'cdef')

    def test_head_matches_range_without_body(self):
        with self.request('/asset/infinex-reference',{'Range':'bytes=10-'},method='HEAD') as response:
            self.assertEqual(response.headers['Content-Length'],'6')
            self.assertEqual(response.read(),b'')

    def test_native_download_preserves_filename_and_extension(self):
        with self.request('/asset/infinex-v05-blend',method='HEAD') as response:
            self.assertEqual(response.headers['Content-Disposition'],"attachment; filename*=UTF-8''phone%20scene.blend")
            self.assertEqual(response.read(),b'')

    def test_invalid_range_returns_416(self):
        for header in ['bytes=99-','bytes=8-2','bytes=0-2,5-8','bytes=-0']:
            with self.subTest(header=header), self.assertRaises(urllib.error.HTTPError) as error:
                self.request('/asset/infinex-reference',{'Range':header})
            self.assertEqual(error.exception.code,416)

    def test_api_has_availability_but_no_private_paths(self):
        with self.request('/api/assets') as response:data=json.load(response)
        self.assertTrue(data['infinex-reference']['available'])
        self.assertFalse(data['infinex-v05-aep']['available'])
        self.assertNotIn(self.temp.name,json.dumps(data))

    def test_unknown_assets_and_directory_browsing_fail(self):
        for path in ['/asset/unknown','/asset/../catalog.json','/library/','/%2e%2e/README.md']:
            with self.subTest(path=path),self.assertRaises(urllib.error.HTTPError) as error:self.request(path)
            self.assertEqual(error.exception.code,404)

    def test_non_loopback_host_is_rejected(self):
        with self.assertRaises(urllib.error.HTTPError) as error:self.request('/api/assets',{'Host':'example.com'})
        self.assertEqual(error.exception.code,403)

    def test_complete_file_and_static_entry(self):
        with self.request('/asset/infinex-reference') as response:self.assertEqual(response.read(),b'0123456789abcdef')
        with self.request('/library/entries/DETAIL-INF-DEFOCUS.json') as response:
            self.assertEqual(json.load(response)['review']['state'],'rejected')


if __name__=='__main__':unittest.main()
