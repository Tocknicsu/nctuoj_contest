data = [
    {
        "name": "test_get_verdict",
        "url": "/api/verdicts/",
        "method": "get",
        "payload": {
            "token": "ADMIN@TOKEN"
        },
        "response_status": 200,
        "response_data": {
            "msg": [{"abbreviation": "Pending", "id": 1, "description": "Pending"}, {"abbreviation": "Judging", "id": 2, "description": "Judging"}, {"abbreviation": "SE", "id": 3, "description": "No - System Error"}, {"abbreviation": "CE", "id": 4, "description": "No - Compile Error"}, {"abbreviation": "RE", "id": 5, "description": "No - Runtime Error"}, {"abbreviation": "MLE", "id": 6, "description": "No - Memory Limit Exceed"}, {"abbreviation": "TLE", "id": 7, "description": "No - Time Limit Exceed"}, {"abbreviation": "OLE", "id": 8, "description": "No - Output Limit Exceed"}, {"abbreviation": "WA", "id": 9, "description": "No - Wrong Answer"}, {"abbreviation": "AC", "id": 10, "description": "Yes - Accepted"}]
        }
    },
]
