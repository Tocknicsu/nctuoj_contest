from req import Service
from permission.base import BasePermission


class Testdata(BasePermission):
    def get(self, req, problem_id):
        pass

    def post(self, req, problem_id):
        if not req.account['isADMIN']:
            return (403, "Permission Denied")

class Testdatum(BasePermission):
    def put(self, req, problem_id, testdata_id):
        if not req.account['isADMIN']:
            return (403, "Permission Denied")

    def delete(self, req, problem_id, testdata_id):
        if not req.account['isADMIN']:
            return (403, "Permission Denied")
