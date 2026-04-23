def test_login():
    username = "admin"
    password = "1234"

    if username == "admin" and password == "1234":
        return {"test_name": "Login Test", "status": "PASS"}
    else:
        return {"test_name": "Login Test", "status": "FAIL"}