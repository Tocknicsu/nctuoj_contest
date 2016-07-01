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
            "msg": {"id": 1, "score_type": 0, "title": "problem A", "executes": [], "testdata": [], "verdict": {"execute_type_id": 2, "id": 1, "file_name": "main.cpp",}}
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
        "name": "post_clarification",
        "url": "/api/clarifications/",
        "method": "post",
        "payload": {
            "token": "ADMIN@TOKEN",
            "problem_id": 1,
            "question": "How are you"
        },
        "response_status": 200,
        "response_data":{
            "msg": {"reply_type": 0, "user_id": 1, "question": "How are you", "problem_id": 1, "reply": "", "id": 1}
        }
    },
    {
        "name": "post_clarification_general",
        "url": "/api/clarifications/",
        "method": "post",
        "payload": {
            "token": "ADMIN@TOKEN",
            "problem_id": 0,
            "question": "How are you"
        },
        "response_status": 200,
        "response_data":{
            "msg": {"reply_type": 0, "user_id": 1, "question": "How are you", "problem_id": 0, "reply": "", "id": 2}
        }
    },
    {
        "name": "post_clarification_no_exist",
        "url": "/api/clarifications/",
        "method": "post",
        "payload": {
            "token": "ADMIN@TOKEN",
            "problem_id": 2,
            "question": "How are you"
        },
        "response_status": 404,
        "response_data":{
            "msg": "Not Found"
        }
    },
    {
        "name": "put_clarification",
        "url": "/api/clarifications/1/",
        "method": "put",
        "payload": {
            "token": "ADMIN@TOKEN",
            "reply_type": 1,
            "reply": "I'm fine."
        },
        "response_status": 200,
        "response_data":{
            "msg": {"problem_id": 1, "user_id": 1, "question": "How are you", "id": 1, "reply_type": 1, "reply": "I'm fine."}
        }
    },
    {
        "name": "put_clarification_again",
        "url": "/api/clarifications/1/",
        "method": "put",
        "payload": {
            "token": "ADMIN@TOKEN",
            "reply_type": 1,
            "reply": "I'm fine."
        },
        "response_status": 403,
        "response_data":{
            "msg": "Permission Denied"
        }
    },
    {
        "name": "put_clarification_no_exist",
        "url": "/api/clarifications/999/",
        "method": "put",
        "payload": {
            "token": "ADMIN@TOKEN",
            "reply_type": 1,
            "reply": "I'm fine."
        },
        "response_status": 404,
        "response_data":{
            "msg": "Not Found"
        }
    }
]
