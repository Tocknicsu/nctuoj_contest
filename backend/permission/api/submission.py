from req import Service
from permission.base import BasePermission

class Submissions(BasePermission):
    def get(self, req):
        pass
    def post(self, req):
        pass


class Submission(BasePermission):
    def exist(self, data={}):
        pass

    def get(self, req, id):
        pass
