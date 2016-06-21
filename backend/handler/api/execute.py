import tornado
import tornado.gen

from req import Service
from req import ApiRequestHandler

class Executes(ApiRequestHandler):
    @tornado.gen.coroutine
    def get(self):
        err, res = yield from Service.Execute.get_execute_list()
        if err: 
            self.render(err)
        else:
            self.render(res)

class Execute(ApiRequestHandler):
    @tornado.gen.coroutine
    def get(self, id):
        err, res = yield from Service.Execute.get_execute({'id': id})
        if err: 
            self.render(err)
        else:
            self.render(res)

    @tornado.gen.coroutine
    def put(self, id):
        args = ['description', 'commands[]']
        data = self.get_args(args)
        data['id'] = id
        err, res = yield from Service.Execute.put_execute(data)
        if err:
            self.render(err)
        else:
            err, res = yield from Service.Execute.get_execute({'id': id})
            self.render(res)
        


