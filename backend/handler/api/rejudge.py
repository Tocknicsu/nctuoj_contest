import tornado
import tornado.gen

from req import Service
from req import ApiRequestHandler

class SubmissionRejudge(ApiRequestHandler):
    @tornado.gen.coroutine
    def post(self, id):
        err, res = yield from Service.Rejudge.rejudge_submission({'id': id})
        if err:
            self.render(err)
        else:
            self.render(res)

class ProblemRejudge(ApiRequestHandler):
    @tornado.gen.coroutine
    def post(self, id):
        err, res = yield from Service.Rejudge.rejudge_problem({'id': id})
        if err:
            self.render(err)
        else:
            self.render(res)
