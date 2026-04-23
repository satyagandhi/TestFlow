def log_result(result):
    with open("logs/test_log.txt", "a") as f:
        f.write(result["test_name"] + " - " + result["status"] + "\n")