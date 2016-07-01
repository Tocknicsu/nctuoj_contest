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
            meta_json = json.loads(meta)
        except:
            self.render((400, "meta.json parse error"))
            return
        self.log(meta_json)
        ### check basic in the meta
        if "basic" not in meta or isinstance(meta['basic'], dict):
            self.render((400, "meta.json not contain basic or basic is not a dict"))
            return

        #err, res = yield from Service.Problem.post_problem(meta['basic'])
        self.render()
        ### remove all tmp file
        try: os.remove(file_path)
        except: pass
        try: shutil.rmtree(unzip_path)
        except: pass



        

class ProblemMeta(ApiRequestHandler):
    @tornado.gen.coroutine
    def put(self):
        args = ['zip[file]']
        data = self.get_args(args)
