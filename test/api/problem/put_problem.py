data = [
    {
        "name": "test_post_problem_admin",
        "url": "/api/problems/",
        "method": "post",
        "payload": {
            "title": "problem A",
            "score_type": 0,
            "token": "ADMIN@TOKEN",
        },
        "files": {
            "pdf": "./api/problem/problem.pdf"
        },
        "response_status": 200,
        "response_data": {
            "msg": {"id": 1, "score_type": 0, "title": "problem A", "testdata": [], "executes": [], "verdict": {"execute_type_id": 2, "id": 1, "file_name": "main.cpp"}}
        }
    }, 
    {
        "name": "test_put_problem_no_login",
        "url": "/api/problems/1/",
        "method": "put",
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
        "name": "test_put_problem_test",
        "url": "/api/problems/1/",
        "method": "put",
        "payload": {
            "title": "problem A",
            "score_type": 1,
            "token": "TEST@TOKEN"
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
        "name": "test_put_problem_unofficical",
        "url": "/api/problems/1/",
        "method": "put",
        "payload": {
            "title": "problem A",
            "score_type": 1,
            "token": "UNOFFICIAL@TOKEN"
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
        "name": "test_put_problem_officical",
        "url": "/api/problems/1/",
        "method": "put",
        "payload": {
            "title": "problem A",
            "score_type": 1,
            "token": "OFFICIAL@TOKEN"
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
        "name": "test_put_problem_admin",
        "url": "/api/problems/1/",
        "method": "put",
        "payload": {
            "title": "problem A",
            "score_type": 1,
            "token": "ADMIN@TOKEN"
        },
        "files": {
            "pdf": "./api/problem/problem.pdf"
        },
        "response_status": 200,
        "response_data": {
            "msg": {"id": 1, "score_type": 1, "title": "problem A", "testdata": [], "executes": [], "verdict": {"execute_type_id": 2, "id": 1, "file_name": "main.cpp"}}
        }
    }, 
    {
        "name": "test_put_problem_admin_no_exist",
        "url": "/api/problems/4/",
        "method": "put",
        "payload": {
            "title": "problem A",
            "score_type": 1,
            "token": "ADMIN@TOKEN"
        },
        "files": {
            "pdf": "./api/problem/problem.pdf"
        },
        "response_status": 404,
        "response_data": {
            "msg": "Not Found"
        }
    }, 
]
