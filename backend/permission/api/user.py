from req import Service
from permission.base import BasePermission


class UsersCSV(BasePermission):
    def post(self, req):
        ### No Login
        if not req.account['isADMIN']:
            return "Permission Denied"
        return None

class Users(BasePermission):
    def get(self, req):
        if not req.account['isADMIN']:
            return "Permission Denied"
        return None

