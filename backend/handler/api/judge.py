import tornado
import tornado.gen

from req import Service
from req import ApiRequestHandler

class JudgeSubmission(ApiRequestHandler):
    @tornado.gen.coroutine
    def get(self):
        err, res = yield from Service.Judge.get_submission()
        if err:
            self.render(err)
        else:
            self.render(res)

    @tornado.gen.coroutine
    def post(self):
        args = ['submission_id']
        data = self.get_args(args)
        self.log(data)
        self.render()

class JudgeSubmissionTestdata(ApiRequestHandler):
    @tornado.gen.coroutine
    def post(self):
        args = ['submission_id', 'testdata_id', 'time_usage', 'memory_usage', 'score', 'verdict_id', 'note']
        data = self.get_args(args)
        err, res = yield from Service.Judge.post_submission_testdata(data)
        if err:
            self.render(err)
        else:
            self.render(res)
            return res

