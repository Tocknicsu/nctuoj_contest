import tornado
import tornado.gen

from req import Service
from req import ApiRequestHandler

class Scoreboard(ApiRequestHandler):
    @tornado.gen.coroutine
    def get(self):
        if self.account['isLOGIN'] == False:
            role = 3
        else:
            role = self.account['type']
        err, res = yield from Service.Scoreboard.get_scoreboard({'type': role})
        if err:
            self.render(err)
        else:
            self.render(res)

    @tornado.gen.coroutine
    def put(self):
        args = ['type']
        data = self.get_args(args)
        err, res = yield from Service.Scoreboard.put_scoreboard(data)
        if err:
            self.render(err)
        else:
            err, res = yield from Service.Scoreboard.get_scoreboard(data)
            self.render(res)
        
