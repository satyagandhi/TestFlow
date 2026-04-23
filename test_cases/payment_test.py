def test_payment():
    amount = 500
    balance = 1000

    if amount <= balance:
        return {"test_name": "Payment Test", "status": "PASS"}
    else:
        return {"test_name": "Payment Test", "status": "FAIL"}