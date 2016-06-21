from req import Service
from permission.base import BasePermission

class Executes(BasePermission):
    def post(self, req):
        if not req.account['isAdmin']:
            return "Permission Denied"
        return None


class Execute(BasePermission):
    def put(self, req):
        pass

    def delete(self, req):
        pass