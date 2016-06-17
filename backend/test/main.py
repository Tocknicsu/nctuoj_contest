#!/usr/bin/env python3
import fnmatch
import json
import os
import requests
import sys

import config

DataType = {
    "name": str,
    "url": str,
    "method": str,
    "payload": dict,
    "response_status": int,
    "response_data": dict,
}

def test(filename):
    print("Test File: %s"%(filename))
    print("=============================")
    try:
        f = open(filename)
    except:
        print("Error: Open Error")
        return
    plaintext = f.read()
    f.close()
    try:
        datalist = json.loads(plaintext)
    except:
        print("Error: Parse To Json Error")
        return
    if not isinstance(datalist, list):
        print("Error: Json is not a list")
        return

    for data in datalist:
        if not isinstance(data, dict):
            print("Error: %s is not dict"%(data))
            return
        for x in DataType:
            if x not in data:
                print("Error: lack %s in %s"%(x, data))
                return
        data['url'] = config.base_url + data['url']
        try:
            func = getattr(requests, data["method"])
        except:
            print("Error: No Such Method %s"%(data['method']))
            return
        if data['method'] == "get":
            response = func(data['url'], params=data['payload'])
        else:
            response = func(data['url'], data=data['payload'])
        try:
            response_json = json.loads(response.text)
        except:
            print("Error: Response Json Parse Error %s"%(response.text))
            return
        if response.status_code != data['response_status'] or response_json != data['response_data']:
            print("Error: Unexpect Response")
            print("Expect: [%s] %s"%(data['response_status'], data['response_data']))
            print("Response: [%s] %s"%(response.status_code, response.text))

if __name__ == '__main__':
    if len(sys.argv) == 1:
        files = []
        for root, dirnames, filenames in os.walk("./"):
            for filename in fnmatch.filter(filenames, '*.json'):
                files.append(os.path.join(root, filename))
    else:
        files = sys.argv[1:]

    for filename in files:
        test(filename)

