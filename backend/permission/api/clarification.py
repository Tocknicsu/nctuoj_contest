from req import Service
from permission.base import BasePermission

class Clarifications(BasePermission):
    def post(self, req):
        if not req.account['isLOGIN']:
            return "Permission Denied"
        return None


class Clarification(BasePermission):
    def put(self, req, id):
        if not req.account['isADMIN']:
            return "Permission Denied"
        return None
