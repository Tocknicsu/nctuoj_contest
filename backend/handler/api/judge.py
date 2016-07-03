import tornado
import tornado.gen

from req import Service
from req import ApiRequestHandler

class JudgeSubmission(ApiRequestHandler):
    @tornado.gen.coroutine
    def get(self):
        err, res = yield from Service.Judge.get_submission()
        self.log(res)
        if err:
            self.render(err)
        else:
            self.render(res)

    def post(self):
        pass

class JudgeSubmissionTestdata(ApiRequestHandler):
    @tornado.gen.coroutine
    def post(self):
        pass
