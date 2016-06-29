import datetime
data = [
    {
        "name": "test_time",
        "url": "/api/system/time/",
        "method": "get",
        "payload": {
        },
        "response_status": 200,
        "response_data": {
            "msg": str(datetime.datetime.now())[:-7]
        }
    }
]
