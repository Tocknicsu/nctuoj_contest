from req import StaticFileHandler
import tornado
import tornado.gen

class TestdatumFile(StaticFileHandler):
    @tornado.gen.coroutine
    def get(self, problem_id, id, file, include_body=True):
        path = '%s/%s' % (id, file)
        yield super().get(path, include_body)
