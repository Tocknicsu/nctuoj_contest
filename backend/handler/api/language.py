import tornado
import tornado.gen

from req import Service
from req import ApiRequestHandler

class Languages(ApiRequestHandler):
    @tornado.gen.coroutine
    def get(self):
        err, res = yield from Service.Language.get_language_list()
        if err:
            self.render(err)
        else:
            self.render(res)
