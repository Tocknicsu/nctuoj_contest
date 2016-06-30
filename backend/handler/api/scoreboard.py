import tornado
import tornado.gen

from req import Service
from req import ApiRequestHandler

class Scoreboard(ApiRequestHandler):
    @tornado.gen.coroutine
    def get(self):
        if self.account['isLOGIN'] == False:
            role = 2
        else:
            role = self.account['type']
        err, res = yield from Service.Scoreboard.get_scoreboard({'type': role})
        if err:
            self.render(err)
        else:
            self.render(res)

    @tornado.gen.coroutine
    def put(self):
        err, res = yield from Service.Contest.put_contest()
        if err:
            self.render(err)
        else:
            err, res = yield from Service.Scoreboard.get_scoreboard()
            self.render(res)
        
