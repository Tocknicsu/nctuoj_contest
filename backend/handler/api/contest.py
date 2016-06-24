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
    def put(self):
        args = ['title', 'description', 'start', 'end', 'freeze']
        data = self.get_args(args)
        err, res = yield from Service.Contest.put_contest(data)
        if err:
            self.render(err)
        else:
            err, res = yield from Service.Contest.get_contest()
            self.render(res)
        
