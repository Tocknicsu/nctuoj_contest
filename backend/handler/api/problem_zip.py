from req import StaticFileHandler
import tornado
import tornado.gen

class ProblemZip(StaticFileHandler):
    @tornado.gen.coroutine
    def get(self, include_body=True):
        yield super().get('problems.zip', include_body)

