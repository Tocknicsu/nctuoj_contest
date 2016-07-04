import tornado
import tornado.gen
import datetime

from req import Service
from req import ApiRequestHandler

class System(ApiRequestHandler):
    @tornado.gen.coroutine
    def get(self, resource=None):
        print(resource)
        if resource == "time":
            err, res = Service.System.get_time()
        elif resource == 'cpu':
            err, res = Service.System.get_cpu()
        elif resource == 'memory':
            err, res = Service.System.get_memory()
        elif resource == 'network':
            err, res = Service.System.get_network()
        else:
            err, res = Service.System.get_all()
        self.render(res)

