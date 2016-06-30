import tornado
import tornado.gen

from req import Service
from req import ApiRequestHandler

class ProblemVerdict(ApiRequestHandler):
    @tornado.gen.coroutine
    def get(self, id):
        err, res = yield from Service.Problem.get_problem_verdict({'id': id})
        if err:
            self.render(err)
        else:
            self.render(res)

    @tornado.gen.coroutine
    def put(self, id):
        args = ['execute_type_id', 'file[file]']
        data = self.get_args(args)
        data['id'] = id
        err, res = yield from Service.Problem.put_problem_verdict(data)
        if err:
            self.render(err)
        else:
            err, res = yield from Service.Problem.get_problem_verdict({'id': id})
            self.render(res)

