from req import Service
from permission.base import BasePermission



class Users(BasePermission):
    def post(self, req):
        if not req.account['isADMIN']:
            return (403, "Permission Denied")

class User(BasePermission):
    def put(self, req, id):
        if not req.account['isADMIN']:
            return (403, "Permission Denied")

    def delete(self, req, id):
        if not req.account['isADMIN']:
            return (403, "Permission Denied")

class UsersCSV(BasePermission):
    def post(self, req):
        if not req.account['isADMIN']:
            return (403, "Permission Denied")

