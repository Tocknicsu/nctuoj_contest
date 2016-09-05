import tornado
import tornado.gen

from req import Service
from req import ApiRequestHandler

class DB(ApiRequestHandler):
    @tornado.gen.coroutine
    def delete(self, name):
        data = {}
        data['name'] = name
        err, res = yield from Service.DB.delete_table(data)
        if err:
            self.render(err)
        else:
            self.render()
