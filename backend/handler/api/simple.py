import tornado
import tornado.gen

from req import Service
from req import ApiRequestHandler

class Simple(ApiRequestHandler):
    @tornado.gen.coroutine
    def get(self):
        err, res = yield from Service.Simple.get_simple()
        self.log("Api Log Test")
        self.render(res)

    @tornado.gen.coroutine
    def post(self):
        args = ['a', 'b']
        data = self.get_args(args)
        err, res = yield from Service.Simple.post_simple(data)
        if err: self.render(err)
        else: self.render(res)

