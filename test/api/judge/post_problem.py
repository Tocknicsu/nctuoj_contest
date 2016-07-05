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
        "ignore": ["id", "user_id"],
        "response_status": 200,
        "response_data":{
            "msg": {
                "length": 141, 
                "score": None, 
                "problem_id": 1,
                "verdict_id": 1, 
                "file_name": "test.cpp", 
                "memory_usage": None, 
                "execute_type_id": 1, 
                "user_id": 1,
                "ip": "127.0.0.1",
                "time_usage": None
            }
        }
    }
]
