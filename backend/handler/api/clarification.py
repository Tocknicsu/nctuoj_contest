import tornado
import tornado.gen

from req import Service
from req import ApiRequestHandler

class Clarifications(ApiRequestHandler):
    @tornado.gen.coroutine
    def get(self):
        pass

    @tornado.gen.coroutine
    def post(self):
        pass

class Clarification(ApiRequestHandler):
    @tornado.gen.coroutine
    def get(self, id):
        pass

    @tornado.gen.coroutine
    def put(self, id):
        pass
        
