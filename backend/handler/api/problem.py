import tornado
import tornado.gen

import hashlib
import config
import zipfile
import os
import shutil
import json

from req import Service
from req import ApiRequestHandler

class Problems(ApiRequestHandler):
    @tornado.gen.coroutine
    def get(self):
        err, res = yield from Service.Problem.get_problem_list()
        if err:
            self.render(err)
        else:
            self.render(res)

    @tornado.gen.coroutine
    def post(self):
        args = ['title', 'pdf[file]', 'score_type']
        data = self.get_args(args)
        err, res = yield from Service.Problem.post_problem(data)
        if err:
            self.render(err)
        else:
            err, res = yield from Service.Problem.get_problem_detail(res)
            self.render(res)

class Problem(ApiRequestHandler):
    @tornado.gen.coroutine
    def get(self, id):
        err, res = yield from Service.Problem.get_problem_detail({'id': id})
        if err:
            self.render(err)
        else:
            self.render(res)

    @tornado.gen.coroutine
    def put(self, id):
        args = ['title', 'pdf[file]', 'score_type']
        data = self.get_args(args)
        data['id'] = id
        err, res = yield from Service.Problem.put_problem(data)
        if err:
            self.render(err)
        else:
            err, res = yield from Service.Problem.get_problem_detail({'id': id})
            self.render(res)
        
class ProblemsMeta(ApiRequestHandler):
    @tornado.gen.coroutine
    def post(self):
        args = ['zip[file]']
        data = self.get_args(args)
        ### gen tmp file name
        filename = hashlib.md5(data['zip']['body']).hexdigest()
        folder = '%s/data/tmp'%(config.DATA_ROOT)
        ### zip file_path
        file_path = '%s/%s'%(folder, filename)
        ### unzip file directory
        unzip_path = '%s/unzip_%s'%(folder, filename)
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
        ### get meta file path
        meta_file_path = "%s/%s"%(unzip_path, "meta.json")
        ### test meta is in the zip
        if not os.path.exists(meta_file_path):
            self.render((400, "meta.json not in the zip"))
            return
        ### parse meta file
        meta = open(meta_file_path, "r").read()
        try:
            meta = json.loads(meta)
        except Exception as e:
            self.log(e)
            self.render((400, "meta.json parse error"+str(e)))
            return
        ### check basic in the meta
        meta['basic']['pdf'] = {}
        meta['basic']['pdf']['filename'] = meta['basic']['file']
        meta['basic']['pdf']['body'] = open("%s/%s"%(unzip_path, meta['basic']['pdf']['filename']), "rb").read()
        if "basic" not in meta or not isinstance(meta['basic'], dict):
            self.render((400, "meta.json not contain basic or basic is not a dict"))
            return

        err, res = yield from Service.Problem.post_problem(meta['basic'])
        problem_id = res['id']
        errlist = []
        if err:
            self.render(err)
        if 'testdata' in meta:
            if not isinstance(meta['testdata'], list):
                errlist += "testdata not a list"
            else:
                for x in meta['testdata']:
                    if 'input' not in x:
                        errlist += "input not in %s"%(x)
                        continue
                    if 'output' not in x:
                        errlist += "output not in %s"%(x)
                        continue
                    _input = x['input']
                    _output = x['output']
                    x['input'] = {}
                    x['input']['filename'] = _input
                    x['input']['body'] = open("%s/%s"%(unzip_path, _input), "rb").read()
                    x['output'] = {}
                    x['output']['filename'] = _output
                    x['output']['body'] = open("%s/%s"%(unzip_path, _output), "rb").read()
                    x['problem_id'] = problem_id
                    err, res = yield from Service.Testdata.post_testdata(x)
                    if err:
                        errlist += err
        if 'executes' in meta:
            if not isinstance(meta['executes'], list):
                errlist += "executes not a list"
            else:
                data = {}
                data['id'] = problem_id
                data['executes'] = meta['executes']
                err, res = yield from Service.Problem.put_problem_execute(data)
                if err:
                    errlist += err

        if 'verdict' in meta:
            if not isinstance(meta['verdict'], dict):
                errlist += 'verdict not a dict'
            else:
                _file = meta['verdict']['file']
                meta['verdict']['file'] = {}
                meta['verdict']['file']['filename'] = _file
                meta['verdict']['file']['body'] = open("%s/%s"%(unzip_path, _file), "rb").read()
                meta['verdict']['id'] = problem_id
                err, res = yield from Service.Problem.put_problem_verdict(meta['verdict'])
                if err:
                    errlist += err + " in the verdict"

        ### remove all tmp file
        try: os.remove(file_path)
        except: pass
        try: shutil.rmtree(unzip_path)
        except: pass
        self.render(errlist)



        

class ProblemMeta(ApiRequestHandler):
    @tornado.gen.coroutine
    def put(self, id):
        args = ['zip[file]']
        data = self.get_args(args)
        ### gen tmp file name
        filename = hashlib.md5(data['zip']['body']).hexdigest()
        folder = '%s/data/tmp'%(config.DATA_ROOT)
        ### zip file_path
        file_path = '%s/%s'%(folder, filename)
        ### unzip file directory
        unzip_path = '%s/unzip_%s'%(folder, filename)
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
        ### get meta file path
        meta_file_path = "%s/%s"%(unzip_path, "meta.json")
        ### test meta is in the zip
        if not os.path.exists(meta_file_path):
            self.render((400, "meta.json not in the zip"))
            return
        ### parse meta file
        meta = open(meta_file_path, "r").read()
        try:
            meta = json.loads(meta)
        except:
            self.render((400, "meta.json parse error"))
            return
        ### check basic in the meta
        meta['basic']['pdf'] = {}
        meta['basic']['pdf']['filename'] = meta['basic']['file']
        meta['basic']['pdf']['body'] = open("%s/%s"%(unzip_path, meta['basic']['pdf']['filename']), "rb").read()
        meta['basic']['id'] = id
        if "basic" not in meta or not isinstance(meta['basic'], dict):
            self.render((400, "meta.json not contain basic or basic is not a dict"))
            return

        err, res = yield from Service.Problem.put_problem(meta['basic'])
        problem_id = id 
        errlist = []
        if err:
            self.render(err)
        if 'testdata' in meta:
            if not isinstance(meta['testdata'], list):
                errlist.append("testdata not a list")
            else:
                for x in meta['testdata']:
                    if 'input' not in x:
                        errlist.append("input not in %s"%(x))
                        continue
                    if 'output' not in x:
                        errlist.append("output not in %s"%(x))
                        continue
                    _input = x['input']
                    _output = x['output']
                    x['input'] = {}
                    x['input']['filename'] = _input
                    x['input']['body'] = open("%s/%s"%(unzip_path, _input), "rb").read()
                    x['output'] = {}
                    x['output']['filename'] = _output
                    x['output']['body'] = open("%s/%s"%(unzip_path, _output), "rb").read()
                    x['problem_id'] = problem_id
                    err, res = yield from Service.Testdata.post_testdata(x)
                    if err:
                        errlista.append(err)
        if 'executes' in meta:
            if not isinstance(meta['executes'], list):
                errlist.append("executes not a list")
            else:
                data = {}
                data['id'] = problem_id
                data['executes'] = meta['executes']
                err, res = yield from Service.Problem.put_problem_execute_list(data)
                if err:
                    errlist.append(err)

        if 'verdict' in meta:
            if not isinstance(meta['verdict'], dict):
                errlist.append('verdict not a dict')
            else:
                _file = meta['verdict']['file']
                meta['verdict']['file'] = {}
                meta['verdict']['file']['filename'] = _file
                meta['verdict']['file']['body'] = open("%s/%s"%(unzip_path, _file), "rb").read()
                meta['verdict']['id'] = problem_id
                err, res = yield from Service.Problem.put_problem_verdict(meta['verdict'])
                if err:
                    errlist.append(err + " in the verdict")

        ### remove all tmp file
        try: os.remove(file_path)
        except: pass
        try: shutil.rmtree(unzip_path)
        except: pass
        self.render(errlist)
