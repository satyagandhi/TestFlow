from test_cases.login_test import test_login
from test_cases.payment_test import test_payment
from test_cases.api_test import test_api
from scripts.defect_tracker import log_result
from scripts.report_generator import generate_report

results = [
    test_login(),
    test_payment(),
    test_api()
]

for result in results:
    log_result(result)

generate_report()

print("Tests completed successfully!")