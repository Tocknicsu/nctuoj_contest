from req import Service
from service.base import BaseService
import config
import os
import shutil
import hashlib
import pyminizip
import json


class Problem(BaseService):
    def get_problem_list(self):
        res = yield self.db.execute("SELECT * FROM problems ORDER BY id ASC")
        res = res.fetchall()
        return (None, res)

    def get_problem(self, data={}):
        required_args = [{
            'name': '+id',
            'type': int,
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        res = yield self.db.execute("SELECT * FROM problems WHERE id=%s", (data['id'],))
        res = res.fetchone()
        return (None, res)

    def get_problem_detail(self, data={}):
        required_args = [{
            'name': '+id',
            'type': int,
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        res = yield self.db.execute("SELECT * FROM problems WHERE id=%s", (data['id'],))
        res = res.fetchone()
        err, res['executes'] = yield from self.get_problem_execute_list(data)
        err, res['testdata'] = yield from Service.Testdata.get_testdata_list(data)
        err, res['verdict'] = yield from self.get_problem_verdict(data)
        return (None, res)

    def post_problem(self, data={}):
        required_args = [{
            'name': '+title',
            'type': str,
        }, {
            'name': '+score_type',
            'type': int
        }, {
            'name': '+pdf',
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        pdf = data.pop('pdf')
        sql, param = self.gen_insert_sql('problems', data)
        res = yield self.db.execute(sql, param)
        res = res.fetchone()
        ### Save File
        yield from self.store_pdf(res['id'], pdf)
        ### Add default verdict
        yield self.db.execute("INSERT INTO verdicts (id, file_name, execute_type_id) VALUES (%s, %s, %s)", (res['id'], "main.cpp", 2,))
        ### copy default verdict file
        folder = os.path.join(config.DATA_ROOT, 'data/verdicts', str(res['id']))
        file_path = os.path.join(folder, 'main.cpp')
        try: os.makedirs(folder)
        except: pass
        shutil.copyfile("./default/verdict/main.cpp", file_path)
        return (None, res)

    def put_problem(self, data):
        required_args = [{
            'name': '+id',
            'type': int
        }, {
            'name': '+title',
            'type': str,
        }, {
            'name': '+score_type',
            'type': int
        }, {
            'name': 'pdf',
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        if 'pdf' in data:
            pdf = data.pop('pdf')
        else:
            pdf = None
        id = data.pop('id')
        sql, param = self.gen_update_sql('problems', data)
        res = yield self.db.execute(sql + ' WHERE id = %s', param + (id,))
        if pdf:
            yield from self.store_pdf(id, pdf)
        return (None, {'id': id})

    def get_problem_execute_list(self, data={}):
        required_args = [{
            'name': '+id',
            'type': int
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        res = yield self.db.execute("SELECT e.id, e.description FROM map_problem_execute as me, execute_types as e WHERE e.id=me.execute_type_id and me.problem_id=%s", (data['id'],))
        res = res.fetchall()
        return (None, res)

    def get_problem_execute(self, data={}):
        required_args = [{
            'name': '+problem_id',
            'type': int
        }, {
            'name': '+execute_type_id',
            'type': int
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        res = yield self.db.execute("SELECT * FROM map_problem_execute WHERE problem_id=%s and execute_type_id=%s", (data['problem_id'], data['execute_type_id'],))
        res = res.fetchone()
        return (None, res)

    def put_problem_execute_list(self, data={}):
        required_args = [{
            'name': '+id',
            'type': int
        }, {
            'name': '+executes',
            'type': list
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        yield self.db.execute("DELETE FROM map_problem_execute WHERE problem_id=%s", (data['id'],))
        for x in data['executes']:
            try:
                yield self.db.execute("INSERT INTO map_problem_execute (problem_id, execute_type_id) VALUES (%s, %s)", (data['id'], x,))
            except:
                pass
        return (None, None)

    def get_problem_verdict(self, data={}):
        required_args = [{
            'name': '+id',
            'type': int
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        res = yield self.db.execute("SELECT * FROM verdicts WHERE id=%s", (data['id'],))
        res = res.fetchone()
        return (None, res)

    def put_problem_verdict(self, data={}):
        required_args = [{
            'name': '+id',
            'type': int,
        }, {
            'name': '+execute_type_id',
            'type': int,
        }, {
            'name': 'file',
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        yield self.db.execute("UPDATE verdicts SET execute_type_id=%s WHERE id=%s",(data['execute_type_id'], data['id']))
        if data['file'] is not None:
            code_file = data.pop('file')
            data['file_name'] = code_file['filename']
            yield self.db.execute("UPDATE verdicts SET file_name=%s WHERE id=%s",(data['file_name'], data['id'],))
            folder = os.path.join(config.DATA_ROOT, 'data/verdicts', str(data['id']))
            file_path = os.path.join(folder, data['file_name'])
            try: shutil.rmtree(folder)
            except: pass
            try: os.makedirs(folder)
            except: pass
            with open(file_path, 'wb+') as f:
                f.write(code_file['body'])
        return (None, None)

    def check_problem_meta(self, data={}):
        required_args = [{
            'name': '+zip',
        }]
        err = self.form_validation(data, required_args)
        if err:
            return (err, None)
        filename = hashlib.md5(data['zip']['body']).hexdigest()
        folder = os.path.join(config.DATA_ROOT, 'data/tmp')
        ### zip file_path
        file_path = os.path.join(folder, filename)
        ### unzip file directory
        unzip_path = os.path.join(folder, 'unzip_%s'%filename)
        try: os.makedirs(folder)
        except: pass
        try: os.makedirs(unzip_path)
        except: pass
        ### save zip file 
        with open(file_path, 'wb+') as f:
            f.write(data['zip']['body'])
        ### unzip 
        try:
            with zipfile.ZipFile(file_path) as f:
                f.extractall(unzip_path)
        except:
            return ((400, 'not a zip file'), None)
        ### get meta file path
        meta_file_path = os.path.join(unzip_path, 'meta.json')
        if not os.path.exists(meta_file_path):
            return ((400, "meta.json not in the zip"), None)
        try:
            meta = json.load(open(os.path.join(unzip_path, 'meta.json'), 'r'))
        except:
            return ((400, "meta.json parse error"), None)
        # check basic
        if "basic" not in meta or not isinstance(meta['basic'], dict):
            return ((400, "meta.json does not contain basic or basic is not a dict"), None)
        required_args = [{
            'name': '+title',
            'type': str,
        }, {
            'name': '+score_type',
            'type': int
        }, {
            'name': '+file',
            'type': str,
        }]
        err = self.form_validation(meta['basic'], required_args)
        if err:
            return ((err[0], 'basic: ' + err[1]), None)
        if not os.path.exists(os.path.join(unzip_path, meta['basic']['file'])):
            return ((400, 'basic: pdf %s does not exist'%meta['basic']['file']), None)
        # check testdata
        if 'testdata' not in meta or not isinstance(meta['testdata'], list):
            return ((400, 'meta.json does not contain testdata or testdata is not a list'))
        for testdatum in meta['testdata']:
            required_args = [{
                'name': '+score',
                'type': int,
            }, {
                'name': '+time_limit',
                'type': int,
            }, {
                'name': '+memory_limit',
                'type': int,
            }, {
                'name': '+output_limit',
                'type': int,
            }, {
                'name': '+input'
            }, {
                'name': '+output'
            }]
            err = self.form_validation(testdatum, required_args)
            if err:
                return ((err[0], 'testdata: ' + err[1]), None)
            # check testdatum input
            if not os.path.exists(os.path.join(unzip_path, testdatum['input'])):
                return ((400, 'testdata: input %s does not exist'%testdatum['input']), none)
            # check testdatum output
            if not os.path.exists(os.path.join(unzip_path, testdatum['output'])):
                return ((400, 'testdata: output %s does not exist'%testdatum['output']), none)
        #check executes
        if 'executes' not in meta or not isinstance(meta['executes'], list):
            return ((400, 'meta.json does not contain executes or executes is not a list'))
        #check verdict(can be ignored)
        if 'verdict' in meta:
            if not isinstance(meta['verdict'], dict):
                return ((400, 'verdict is not a dict'), None)
            required_args = [{
                'name': '+execute_type_id',
                'type': int,
            }]
            rer = self.form_validation(meta['verdict'], required_args)
            if err:
                return ((err[0], 'verdict: ' + err[1]))
        #remove temp file
        try: os.remove(file_path)
        except: pass
        try: shutil.rmtree(unzip_path)
        except: pass
        return (None, None)
    
    def post_problem_meta(self, data={}):
        required_args = [{
            'name': '+zip',
        }]
        err = self.form_validation(data, required_args)
        if err:
            return (err, None)
        filename = hashlib.md5(data['zip']['body']).hexdigest()
        folder = os.path.join(config.DATA_ROOT, 'data/tmp')
        ### zip file_path
        file_path = os.path.join(folder, filename)
        ### unzip file directory
        unzip_path = os.path.join(folder, 'unzip_%s'%filename)
        try: os.makedirs(folder)
        except: pass
        try: os.makedirs(unzip_path)
        except: pass
        ### save zip file 
        with open(file_path, 'wb+') as f:
            f.write(data['zip']['body'])
        ### unzip 
        with zipfile.ZipFile(file_path) as f:
            f.extractall(unzip_path)
        meta = json.load(open(os.path.join(unzip_path, 'meta.json'), 'r'))
        #proccess basic
        basic = meta['basic']
        basic['pdf'] = {}
        basic['pdf']['filename'] = basic['file']
        basic['pdf']['body'] = open(os.path.join(unzip_path, basic['pdf']['filename']), 'rb').read()
        err, res = yield from Service.Problem.post_problem(meta['basic'])
        if err:
            return ((err[0], 'basic: ' + err[1]), None)
        problem_id = res['id']
        errlist = []
        #proccess testdata
        yield self.db.execute('DELETE FROM testdata WHERE problem_id = %s;', (problem_id,))
        for testdatum in meta['testdata']:
            _input = testdatum['input']
            testdatum['input'] = {}
            testdatum['input']['filename'] = _input
            testdatum['input']['body'] = open(os.path.join(unzip_path, testdatum['input']['filename']), 'rb').read()
            _output = testdatum['output']
            testdatum['output'] = {}
            testdatum['output']['filename'] = _output
            testdatum['output']['body'] = open(os.path.join(unzip_path, testdatum['output']['filename']), 'rb').read()
            testdatum['problem_id'] = problem_id
            err, res = yield from Service.Testdata.post_testdata(testdatum)
            if err:
                errlist.append('testdata: ' + err[1])
        #proccess executes
        data = {}
        data['id'] = problem_id
        data['executes'] = meta['executes']
        err, res = yield from Service.Problem.put_problem_execute_list(data)
        if err:
            errlist.append('execute: ' + err[1])
        #proccess verdict
        if 'verdict' in meta:
            verdict = meta['verdict']
            verdict['file'] = {'filename': verdict['file']}
            verdict['file']['body'] = open(os.path.join(unzip_path, verdict['file']['filename']), 'rb').read()
            verdict['id'] = problem_id
            err, res = yield from Service.Problem.put_problem_verdict(verdict)
            if err:
                errlist.append('verdict: ' + err[1])
        #remove temp file
        try: os.remove(file_path)
        except: pass
        try: shutil.rmtree(unzip_path)
        except: pass
        if len(errlist) == 0:
            return (None, {'id': problem_id})
        else:
            return (errlist, None)


    def put_problem_meta(self, data={}):
        required_args = [{
            'name': '+zip',
        }, {
            'name': '+id',
            'type': int,
        }]
        err = self.form_validation(data, required_args)
        if err:
            return (err, None)
        filename = hashlib.md5(data['zip']['body']).hexdigest()
        folder = os.path.join(config.DATA_ROOT, 'data/tmp')
        ### zip file_path
        file_path = os.path.join(folder, filename)
        ### unzip file directory
        unzip_path = os.path.join(folder, 'unzip_%s'%filename)
        try: os.makedirs(folder)
        except: pass
        try: os.makedirs(unzip_path)
        except: pass
        ### save zip file 
        with open(file_path, 'wb+') as f:
            f.write(data['zip']['body'])
        ### unzip 
        with zipfile.ZipFile(file_path) as f:
            f.extractall(unzip_path)
        meta = json.load(open(os.path.join(unzip_path, 'meta.json'), 'r'))
        #proccess basic
        basic = meta['basic']
        basic['id'] = data['id']
        basic['pdf'] = {}
        basic['pdf']['filename'] = basic['file']
        basic['pdf']['body'] = open(os.path.join(unzip_path, basic['pdf']['filename']), 'rb').read()
        err, res = yield from Service.Problem.put_problem(meta['basic'])
        if err:
            return ((err[0], 'basic: ' + err[1]), None)
        problem_id = res['id']
        errlist = []
        #proccess testdata
        yield self.db.execute('DELETE FROM testdata WHERE problem_id = %s;', (problem_id,))
        for testdatum in meta['testdata']:
            _input = testdatum['input']
            testdatum['input'] = {}
            testdatum['input']['filename'] = _input
            testdatum['input']['body'] = open(os.path.join(unzip_path, testdatum['input']['filename']), 'rb').read()
            _output = testdatum['output']
            testdatum['output'] = {}
            testdatum['output']['filename'] = _output
            testdatum['output']['body'] = open(os.path.join(unzip_path, testdatum['output']['filename']), 'rb').read()
            testdatum['problem_id'] = problem_id
            err, res = yield from Service.Testdata.post_testdata(testdatum)
            if err:
                errlist.append('testdata: ' + err[1])
        #proccess executes
        data = {}
        data['id'] = problem_id
        data['executes'] = meta['executes']
        err, res = yield from Service.Problem.put_problem_execute_list(data)
        if err:
            errlist.append('execute: ' + err[1])
        #proccess verdict
        if 'verdict' in meta:
            verdict = meta['verdict']
            verdict['file'] = {'filename': verdict['file']}
            verdict['file']['body'] = open(os.path.join(unzip_path, verdict['file']['filename']), 'rb').read()
            verdict['id'] = problem_id
            err, res = yield from Service.Problem.put_problem_verdict(verdict)
            if err:
                errlist.append('verdict: ' + err[1])
        #remove temp file
        try: os.remove(file_path)
        except: pass
        try: shutil.rmtree(unzip_path)
        except: pass
        if len(errlist) == 0:
            return (None, {'id': problem_id})
        else:
            return (errlist, None)

    def store_pdf(self, id, pdf):
        folder = os.path.join(config.DATA_ROOT, 'data/problems')
        file_path = os.path.join(folder, "%s.pdf"%chr(ord('A')+id-1))
        try: os.makedirs(folder)
        except: pass
        with open(file_path, 'wb+') as f:
            f.write(pdf['body'])
        err, res = yield from self.gen_zip()
        return (err, None)


    def gen_zip(self):
        err, problems = yield from self.get_problem_list()
        if err:
            return (err, None)
        folder = os.path.join(config.DATA_ROOT, 'data/problems')
        problem_list = [ os.path.join(folder, "%s.pdf"%chr(ord('A')+problem['id']-1)) for problem in problems]
        self.log(problem_list)
        zip_path = os.path.join(config.DATA_ROOT, 'data/problems/problems.zip')

        pyminizip.compress_multiple(problem_list, zip_path, '12345', 5)
        return (None, None)

