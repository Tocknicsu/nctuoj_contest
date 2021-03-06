import tornado
import tornado.gen

from req import Service
from req import ApiRequestHandler

class ProblemExecutes(ApiRequestHandler):
    @tornado.gen.coroutine
    def get(self, id):
        err, res = yield from Service.Problem.get_problem_execute_list({'id': id})
        if err:
            self.render(err)
        else:
            self.render(res)

    @tornado.gen.coroutine
    def put(self, id):
        args = ['executes[]']
        data = self.get_args(args)
        data['id'] = id
        err, res = yield from Service.Problem.put_problem_execute_list(data)
        if err:
            self.render(err)
        else:
            err, res = yield from Service.Problem.get_problem_execute_list({'id': id})
            self.render(res)

