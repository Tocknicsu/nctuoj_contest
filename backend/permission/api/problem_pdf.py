from req import Service
from permission.base import BasePermission


class ProblemPdf(BasePermission):
    def exist(self, data={}):
        err, res = yield from Service.Problem.get_problem(data)
        if res is None:
            return (404, "Not Found")

    
    def get(self, req, id):
        err = yield from self.exist({'id': id})
        if err:
            return err
