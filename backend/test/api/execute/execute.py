#!/usr/bin/env python3
import sys
import requests
import json
import unittest
import datetime
from util import TestCase
import config

class TestApiExecute(TestCase):
    url = "%s/api/executes/1/"%(config.base_url,)

    def test_get(self):
        res = requests.get(self.url)
        res.connection.close()
        expect_result = {
            "status_code": 200,
            "body": {
                "msg": [{"command": "gcc -lm -std=c99 __FILE__"}, {"command": "./a.out"}]
            }
        }
        self.assertEqualR(res, expect_result)
