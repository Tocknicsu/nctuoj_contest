#!/usr/bin/env python3
import requests
import config
import time
import datetime

def tick_user(Type):
    data = {
        "token": config.sb_token,
        "type": Type
    }
    url = "%s/api/scoreboard/"%(config.base_url,)
    r = requests.put(url, data=data)
    print("[%s] [%s] %s"%(str(datetime.datetime.now())[:-7], r.status_code, str(data)))

if __name__ == "__main__":
    while True:
        try:
            for i in range(4):
                tick_user(i)
        except Exception as e:
            print(e)
        time.sleep(3)


