data = [
    {
        "name": "test_post_problem_admin",
        "url": "/api/problems/meta/",
        "method": "post",
        "payload": {
            "token": "ADMIN@TOKEN",
        },
        "files": {
            "zip": "./api/problem_meta/problem_meta.zip"
        },
        "response_status": 200,
        "response_data": {
            "msg": ""
        }
    }, 
    {
        "name": "test_put_problem_admin",
        "url": "/api/problems/1/meta/",
        "method": "put",
        "payload": {
            "token": "ADMIN@TOKEN",
        },
        "files": {
            "zip": "./api/problem_meta/problem_meta.zip"
        },
        "response_status": 200,
        "response_data": {
            "msg": ""
        }
    }, 
]
