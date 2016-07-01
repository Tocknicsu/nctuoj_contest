import tornado
import tornado.gen

from req import Service
from req import ApiRequestHandler
from req import StaticFileHandler

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

class ProblemVerdictFile(StaticFileHandler):
    @tornado.gen.coroutine
    def get(self, id, include_body=True):
        path = ''
        err, res = yield from Service.Problem.get_problem_verdict({'id': id})
        path = '%s/%s' % (id, res['file_name'])
        yield super().get(path, include_body)
