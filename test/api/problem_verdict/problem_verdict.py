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
            "msg": {"id": 1, "score_type": 0, "title": "problem A", "executes": [], "testdata": []}
        }
    },
    {
        "name": "get_problem_verdict",
        "url": "/api/problems/1/verdict/",
        "method": "get",
        "payload": {
            "token": "ADMIN@TOKEN",
        },
        "response_status": 200,
        "response_data": {
        }
    },
]