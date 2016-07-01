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
            "msg": {"id": 1, "score_type": 0, "title": "problem A", "testdata": [], "executes": []}
        }
    }, 
    {
        "name": "test_post_problem_admin",
        "url": "/api/problems/meta/",
        "method": "post",
        "payload": {
            "token": "ADMIN@TOKEN",
        },
        "files": {
            "zip": "./api/problem_meta/problem_meta_without_meta_json.zip"
        },
        "response_status": 400,
        "response_data": {
            "msg": "meta.json not in the zip"
        }
    }, 
    {
        "name": "test_post_problem_admin",
        "url": "/api/problems/meta/",
        "method": "post",
        "payload": {
            "token": "ADMIN@TOKEN",
        },
        "files": {
            "zip": "./api/problem_meta/problem_meta_error_json.zip"
        },
        "response_status": 400,
        "response_data": {
            "msg": "meta.json parse error"
        }
    },
]
