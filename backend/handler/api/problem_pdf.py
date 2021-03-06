from req import StaticFileHandler
import tornado
import tornado.gen

class ProblemPdf(StaticFileHandler):
    @tornado.gen.coroutine
    def get(self, path, include_body=True):
        # path += '/pdf.pdf'
        path = chr(ord('A') + int(path) - 1) + '.pdf'
        yield super().get(path, include_body)

