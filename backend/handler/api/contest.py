import tornado
import tornado.gen

from req import Service
from req import ApiRequestHandler

class Contest(ApiRequestHandler):
    @tornado.gen.coroutine
    def get(self):
        err, res = yield from Service.Contest.get_contest()
        if err:
            self.render(err)
        else:
            self.render(res)

    @tornado.gen.coroutine
    def put(self, id):
        pass
        
