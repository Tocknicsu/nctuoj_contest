import tornado
import tornado.gen
import datetime

from req import Service
from req import ApiRequestHandler

class System(ApiRequestHandler):
    @tornado.gen.coroutine
    def get(self, resource):
        print(resource)
        if resource == "time":
            self.render(datetime.datetime.now())
        else:
            self.write_error(404)

