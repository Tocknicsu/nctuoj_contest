from req import Service
from permission.base import BasePermission



class Users(BasePermission):
    def get(self, req):
        if not req.account['isADMIN']:
            return (403, "Permission Denied")

    def post(self, req):
        if not req.account['isADMIN']:
            return (403, "Permission Denied")

class UsersCSV(BasePermission):
    def post(self, req):
        if not req.account['isADMIN']:
            return (403, "Permission Denied")
