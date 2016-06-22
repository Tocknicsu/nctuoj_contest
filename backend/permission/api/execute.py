from req import Service
from permission.base import BasePermission

class Executes(BasePermission):
    def post(self, req):
        if not req.account['isADMIN']:
            return (403, "Permission Denied")


class Execute(BasePermission):
    def exist(self, data={}):
        err, res = yield from Service.Execute.get_execute(data)
        if res is None:
            return (404, "Not Found")

    
    def get(self, req, id):
        err = yield from self.exist({'id': id})
        if err:
            return err

    def put(self, req, id):
        if not req.account['isADMIN']:
            return (403, "Permission Denied")
        err = yield from self.exist({'id': id})
        if err:
            return err

    def delete(self, req, id):
        if not req.account['isADMIN']:
            return (403, "Permission Denied")
        err = yield from self.exist({'id': id})
        if err:
            return err
