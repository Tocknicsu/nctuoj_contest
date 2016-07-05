data = [
    {
        "name": "test_post_problem_admin",
        "url": "/api/problems/meta/",
        "method": "post",
        "payload": {
            "token": "ADMIN@TOKEN",
        },
        "files": {
            "zip": "./api/judge/problem_meta/problem_meta.zip"
        },
        "response_status": 200,
        "response_data": {
            "msg": []
        }
    }, 
    {
        "name": "post_submission",
        "url": "/api/submissions/",
        "method": "post",
        "files": {
            "file": "./api/judge/test.cpp",
        },
        "payload": {
            "problem_id": 1,
            "execute_type_id": 2,
            "token": "ADMIN@TOKEN",
        },
        "ignore": ["msg"],
        "response_status": 200,
        "response_data":{
        }
    },
    {
        "name": "post_submission",
        "url": "/api/submissions/",
        "method": "post",
        "files": {
            "file": "./api/judge/ce.cpp",
        },
        "payload": {
            "problem_id": 1,
            "execute_type_id": 2,
            "token": "ADMIN@TOKEN",
        },
        "ignore": ["msg"],
        "response_status": 200,
        "response_data":{
        }
    }
]
