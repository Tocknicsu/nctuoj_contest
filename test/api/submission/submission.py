def problem_data():
    data = []
    for i in range(1, 5):
        data += [{
            "name": "post_problem_%s"%(chr(ord('A')+i-1)),
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
            "url": "/api/problems/%s/executes/"%(i),
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
    role_token = ["admin", "test", "unofficial", "official"]
    for x in role_token:
        for i in range(1, 5):
            data += [{
                "name": "post_submission_%s_%s"%(x, chr(ord('A')+i-1)),
                "url": "/api/submissions/",
                "method": "post",
                "payload": {
                    "problem_id": i,
                    "execute_type_id": 1,
                    "file_name": "test.c",
                    "code": "#include <stdio.h>\n int main(){ printf(\"Hello World\"); }",
                    "token": "%s@TOKEN"%(x.upper()),
                },
                "ignore": ["msg"],
                "response_status": 200,
                "response_data":{}

            }]
    return data

def query_submissions():
    data = []
    role_token = ["admin", "test", "unofficial", "official"]
    for x in role_token:
        data += [
            {
                "name": "get_submission_%s"%(x),
                "url": "/api/submissions/",
                "method": "get",
                "payload":{
                    "count": 10,
                    "page": 1,
                    "token": "%s@TOKEN"%(x.upper()),
                },
                "response_status": 200,
                "response_data": {
                }
            },
        ]
    return data

data = []
data += problem_data()
data += post_submission()
data += query_submissions()
