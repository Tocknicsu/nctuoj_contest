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
        err, res = Service.Problem.check_problem_meta(data)
        if err:
            self.render(err)
            return

        err, res = yield from Service.Problem.post_problem_meta(data)
        if err:
            self.render(err)
        else:
            err, res = yield from Service.Problem.get_problem_detail(res)
            self.render(res)



        

class ProblemMeta(ApiRequestHandler):
    @tornado.gen.coroutine
    def put(self, id):
        args = ['zip[file]']
        data = self.get_args(args)
        err, res = Service.Problem.check_problem_meta(data)
        if err:
            self.render(err)
            return
        data['id'] = id
        err, res = yield from Service.Problem.put_problem_meta(data)
        if err:
            self.render(err)
        else:
            err, res = yield from Service.Problem.get_problem_detail(data)
            self.render(res)
