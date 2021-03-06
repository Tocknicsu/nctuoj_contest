import tornado
import tornado.gen

from req import Service
from req import ApiRequestHandler

class Testdata(ApiRequestHandler):
    @tornado.gen.coroutine
    def get(self, problem_id):
        err, res = yield from Service.Testdata.get_testdata_list({'id': problem_id})
        if err:
            self.render(err)
        else:
            self.render(res)

    @tornado.gen.coroutine
    def post(self, problem_id):
        args = ['score', 'time_limit', 'memory_limit', 'output_limit', 'input[file]', 'output[file]']
        data = self.get_args(args)
        data['problem_id'] = problem_id
        err, res = yield from Service.Testdata.post_testdata(data)
        if err:
            self.render(err)
        else:
            err, res = yield from Service.Testdata.get_testdata(res)
            self.render(res)

class Testdatum(ApiRequestHandler):
    @tornado.gen.coroutine
    def get(self, problem_id, testdata_id):
        err, res = yield from Service.Testdata.get_testdata({'id': testdata_id})
        if err:
            self.render(err)
        else:
            self.render(res)

    @tornado.gen.coroutine
    def put(self, problem_id, testdata_id):
        args = ['score', 'time_limit', 'memory_limit', 'output_limit', 'input[file]', 'output[file]']
        data = self.get_args(args)
        data['id'] = testdata_id
        err, res = yield from Service.Testdata.put_testdata(data)
        if err:
            self.render(err)
        else:
            err, res = yield from Service.Testdata.get_testdata({'id': testdata_id})
            self.render(res)

    @tornado.gen.coroutine
    def delete(self, problem_id, testdata_id):
        err, res = yield from Service.Testdata.delete_testdata({'id': testdata_id})
        if err:
            self.render(err)
        else:
            self.render(res)

