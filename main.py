import pytest


def run_tests():
    """Function to run all test cases"""
    pytest.main(['test_cases.py'])


def generate_report():
    """Generate test report"""
    pytest.main(["test_cases.py", "--html=test_report.html"])


if __name__ == "__main__":
    run_tests()
    generate_report()