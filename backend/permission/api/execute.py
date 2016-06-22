from req import Service
from permission.base import BasePermission

class Executes(BasePermission):
    def post(self, req):
        if not req.account['isADMIN']:
            return "Permission Denied"
        return None


class Execute(BasePermission):
    def put(self, req):
        if not req.account['isADMIN']:
            return "Permission Denied"
        return None

    def delete(self, req):
        if not req.account['isADMIN']:
            return "Permission Denied"
        return None
