from req import Service
from permission.base import BasePermission


class TestdatumFile(BasePermission):
    def get(self, req, problem_id, id, file):
        if req.account['isADMIN'] == False:
            return (403, "Permission Denied")
