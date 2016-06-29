data = [
    {
        "name": "post_problem",
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
        "response_status": 200,
        "response_data": {
            "msg": {"id": 1, "score_type": 0, "title": "problem A", "testdata": [], "executes": []}
        }
    },
    {
        "name": "put_problem_execute",
        "url": "/api/problems/1/executes/",
        "method": "put",
        "payload": {
            "token": "ADMIN@TOKEN",
            "executes[]": [1, 2, 3, 4]
        },
        "response_status": 200,
        "response_data": {
            "msg": [{"description": "C", "id": 1}, {"description": "C++11", "id": 2}, {"description": "C++14", "id": 3}, {"description": "Java", "id": 4}]
        }
    },
    {
        "name": "post_submission",
        "url": "/api/submissions/",
        "method": "post",
        "payload": {
            "token": "ADMIN@TOKEN",
            "problem_id": 1,
            "execute_type_id": 1,
            "file_name": "test.c",
            "code": "#include <stdio.h>\n int main(){ printf(\"Hello World\"); }"
        },
        "response_status": 200,
        "response_data":{
            "msg": {
                "problem_id": 1, 
                "length": 56, 
                "memory_usage": None, 
                "file_name": "test.c", 
                "user_id": 1, 
                "time_usage": None, 
                "ip": "127.0.0.1", 
                "id": 1, 
                "execute_type_id": 1, 
                "verdict": 1, 
                "score": None,
            }
        }
    },
    {
        "name": "post_submission_file",
        "url": "/api/submissions/",
        "method": "post",
        "files": {
            "file": "./api/submission/submission.c"
        },
        "payload": {
            "token": "ADMIN@TOKEN",
            "problem_id": 1,
            "execute_type_id": 1
        }, 
        "response_status": 200,
        "response_data": {
            "msg": {
                "problem_id": 1, 
                "length": 76, 
                "memory_usage": None, 
                "file_name": "submission.c", 
                "user_id": 1, 
                "time_usage": None, 
                "ip": "127.0.0.1", 
                "id": 2, 
                "execute_type_id": 1, 
                "verdict": 1, 
                "score": None,
            }
        }
    }
]
