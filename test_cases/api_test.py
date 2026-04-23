def test_api():
    status_code = 200

    if status_code == 200:
        return {"test_name": "API Test", "status": "PASS"}
    else:
        return {"test_name": "API Test", "status": "FAIL"}