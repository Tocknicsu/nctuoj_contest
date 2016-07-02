def set_contest():
    import datetime
    start = datetime.datetime.now() + datetime.timedelta(hours=-4)
    end = datetime.datetime.now() + datetime.timedelta(hours=-1)
    start = str(start)[:-7]
    end = str(end)[:-7]
    return [{
        "name": "adjust to now before contest",
        "url": "/api/contest/",
        "method": "put",
        "payload": {
            "token": "ADMIN@TOKEN",
            "title": "change",
            "start": start,
            "end": end,
            "freeze": 0,
            "description": "XD"
        },
        "response_status": 200,
        "response_data": {
            "msg": {
                "title": "change",
                "start": start,
                "end": end,
                "freeze": 0,
                "description": "XD"
            }
        }
    },]

def problem_data():
    data = []
    data += [{
        "name": "post_problem_A",
        "url": "/api/problems/",
        "method": "post",
        "payload": {
            "token": "ADMIN@TOKEN",
            "title": "problem A",
            "score_type": 0
        },
        "files": {
            "pdf": "./api/problem/problem.pdf"
        },
        "ignore": ["msg"],
        "response_status": 200,
        "response_data": {}
    },
    {
        "name": "put_problem_execute",
        "url": "/api/problems/1/executes/",
        "method": "put",
        "payload": {
            "token": "ADMIN@TOKEN",
            "executes[]": [1, 2, 3, 4]
        },
        "ignore": ["msg"],
        "response_status": 200,
        "response_data": {}
    }]
    return data

def post_submission():
    data = []
    role_token = ["admin"]
    for x in role_token:
        data += [{
            "name": "post_submission_%s"%(x),
            "url": "/api/submissions/",
            "method": "post",
            "payload": {
                "problem_id": 1,
                "execute_type_id": 1,
                "file_name": "test.c",
                "code": "#include <stdio.h>\n int main(){ printf(\"Hello World\"); }",
                "token": "%s@TOKEN"%(x.upper()),
            },
            "ignore": ["id", "user_id"],
            "response_status": 200,
            "response_data":{
                "msg": {
                    "length": 56, 
                    "score": None, 
                    "problem_id": 1,
                    "verdict_id": 1, 
                    "file_name": "test.c", 
                    "memory_usage": None, 
                    "execute_type_id": 1, 
                    "user_id": 1,
                    "ip": "127.0.0.1",
                    "time_usage": None
                }
            }
        }]
    role_token = ["test", "unofficial", "official"]
    for x in role_token:
        data += [{
            "name": "post_submission_%s"%(x),
            "url": "/api/submissions/",
            "method": "post",
            "payload": {
                "problem_id": 1,
                "execute_type_id": 1,
                "file_name": "test.c",
                "code": "#include <stdio.h>\n int main(){ printf(\"Hello World\"); }",
                "token": "%s@TOKEN"%(x.upper()),
            },
            "ignore": ["id", "user_id"],
            "response_status": 403,
            "response_data":{
                "msg": "Permission Denied"
            }
        }]
    return data

data = []
data += set_contest()
data += problem_data()
data += post_submission()
