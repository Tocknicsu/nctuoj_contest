import tornado
import tornado.gen

from req import Service
from req import ApiRequestHandler

class Verdicts(ApiRequestHandler):
    @tornado.gen.coroutine
    def get(self):
        err, res = yield from Service.Verdict.get_verdict_list()
        if err:
            self.render(err)
        else:
            self.render(res)

