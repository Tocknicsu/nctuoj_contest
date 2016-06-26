import tornado
import tornado.gen

from req import Service
from req import ApiRequestHandler

class ProblemExecutes(ApiRequestHandler):
    @tornado.gen.coroutine
    def get(self, id):
        err, res = yield from Service.Problem.get_problem_execute({'id': id})
        if err:
            self.render(err)
        else:
            self.render(res)

    @tornado.gen.coroutine
    def put(self, id):
        err, res = yield from Service.Problem.put_problem_execute({'id': id})
        if err:
            self.render(err)
        else:
            err, res = yield from Service.Problem.get_problem_execute({'id': id})
            self.render(res)

