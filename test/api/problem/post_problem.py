data = [
    {
        "name": "test_post_problem",
        "url": "/api/problems/",
        "method": "post",
        "payload": {
            "title": "problem A",
            "score_type": 0
        },
        "files": {
            "pdf": "./api/problem/problem.pdf"
        },
        "response_status": 403,
        "response_data": {
            "msg": "Permission Denied"
        }
    }, 
    {
        "name": "test_post_problem_test",
        "url": "/api/problems/",
        "method": "post",
        "payload": {
            "token": "TEST@TOKEN",
            "title": "problem A",
            "score_type": 0
        },
        "files": {
            "pdf": "./api/problem/problem.pdf"
        },
        "response_status": 403,
        "response_data": {
            "msg": "Permission Denied"
        }
    }, 
    {
        "name": "test_post_problem_unofficial",
        "url": "/api/problems/",
        "method": "post",
        "payload": {
            "token": "UNOFFICIAL@TOKEN",
            "title": "problem A",
            "score_type": 0
        },
        "files": {
            "pdf": "./api/problem/problem.pdf"
        },
        "response_status": 403,
        "response_data": {
            "msg": "Permission Denied"
        }
    }, 
    {
        "name": "test_post_problem_official",
        "url": "/api/problems/",
        "method": "post",
        "payload": {
            "token": "OFFICIAL@TOKEN",
            "title": "problem A",
            "score_type": 0
        },
        "files": {
            "pdf": "./api/problem/problem.pdf"
        },
        "response_status": 403,
        "response_data": {
            "msg": "Permission Denied"
        }
    }, 
    {
        "name": "test_post_problem_admin",
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
            "msg": {"id": 1, "score_type": 0, "title": "problem A", "testdata": [], "executes": [], "verdict": {"execute_type_id": 2, "id": 1, "file_name": "main.cpp"}}
        }
    },
]
