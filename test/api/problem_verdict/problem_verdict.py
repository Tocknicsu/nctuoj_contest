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
            "msg": {"id": 1, "score_type": 0, "title": "problem A", "executes": [], "testdata": [], "verdict": {"execute_type_id": 2, "id": 1, "file_name": "main.cpp"}}
        }
    },
    {
        "name": "get_problem_verdict_no_login",
        "url": "/api/problems/1/verdict/",
        "method": "get",
        "payload": {
        },
        "response_status": 403,
        "response_data": {
            "msg": "Permission Denied"
        }
    },
    {
        "name": "get_problem_verdict_test",
        "url": "/api/problems/1/verdict/",
        "method": "get",
        "payload": {
            "token": "TEST@TOKEN",
        },
        "response_status": 403,
        "response_data": {
            "msg": "Permission Denied"
        }
    },
    {
        "name": "get_problem_verdict_unofficial",
        "url": "/api/problems/1/verdict/",
        "method": "get",
        "payload": {
            "token": "UNOFFICIAL@TOKEN",
        },
        "response_status": 403,
        "response_data": {
            "msg": "Permission Denied"
        }
    },
    {
        "name": "get_problem_verdict_official",
        "url": "/api/problems/1/verdict/",
        "method": "get",
        "payload": {
            "token": "OFFICIAL@TOKEN"
        },
        "response_status": 403,
        "response_data": {
            "msg": "Permission Denied"
        }
    },
    {
        "name": "get_problem_verdict_admin",
        "url": "/api/problems/1/verdict/",
        "method": "get",
        "payload": {
            "token": "ADMIN@TOKEN",
        },
        "response_status": 200,
        "response_data": {
            "msg": {"execute_type_id": 2, "id": 1, "file_name": "main.cpp"}
        }
    },
    {
        "name": "get_problem_verdict_admin_no_exist",
        "url": "/api/problems/2/verdict/",
        "method": "get",
        "payload": {
            "token": "ADMIN@TOKEN",
        },
        "response_status": 404,
        "response_data": {
            "msg": "Not Found"
        }
    },
]
