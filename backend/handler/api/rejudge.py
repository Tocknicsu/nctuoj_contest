import tornado
import tornado.gen

from req import Service
from req import ApiRequestHandler

class SubmissionRejudge(ApiRequestHandler):
    @tornado.gen.coroutine
    def post(self, id):
        err, res = yield from Service.Rejudge.submission_rejudge({'id': id})
        if err:
            self.render(err)
        else:
            self.render(res)

class ProblemRejudge(ApiRequestHandler):
    @tornado.gen.coroutine
    def post(self, id):
        err, res = yield from Service.Rejudge.problem_rejudge({'id': id})
        if err:
            self.render(err)
        else:
            self.render(res)
