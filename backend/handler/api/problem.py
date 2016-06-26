import tornado
import tornado.gen

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
            err, res = yield from Service.Problem.get_problem(res)
            self.render(res)

class Problem(ApiRequestHandler):
    @tornado.gen.coroutine
    def get(self, id):
        err, res = yield from Service.Problem.get_problem({'id': id})
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
            err, res = yield from Service.Problem.get_problem({'id': id})
            self.render(res)
        
