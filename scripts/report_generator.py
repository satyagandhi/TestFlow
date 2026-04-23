def generate_report():
    passed = 0
    failed = 0

    with open("logs/test_log.txt", "r") as f:
        lines = f.readlines()

    for line in lines:
        if "PASS" in line:
            passed += 1
        else:
            failed += 1

    with open("reports/test_report.txt", "w") as r:
        r.write("Passed: " + str(passed) + "\n")
        r.write("Failed: " + str(failed))