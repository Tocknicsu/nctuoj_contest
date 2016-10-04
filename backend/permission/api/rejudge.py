from req import Service
from permission.base import BasePermission


class SubmissionRejudge(BasePermission):
    def post(self, req, id):
        if not req.account['isADMIN']:
            return (403, "Permission Denied")

class ProblemRejudge(BasePermission):
    def post(self, req, id):
        if not req.account['isADMIN']:
            return (403, "Permission Denied")

