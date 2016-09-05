import tornado
import tornado.gen

from req import Service
from req import ApiRequestHandler

class DB(ApiRequestHandler):
    @tornado.gen.coroutine
    def delete(self, name):
        self.render()
