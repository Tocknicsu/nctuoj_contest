import requests
import json
import unittest
import subprocess as sp
class TestCase(unittest.TestCase):
    def assertEqualR(self, r, data={}, json_equal=True):
        self.assertEqual(r.status_code, int(data['status_code']))
        body = r.text
        if json_equal: body = json.loads(body)
        self.assertEqual(body, data['body'])
