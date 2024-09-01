# Q:- What is soft assertion in Selenium? How can you mark a test case as failed by using soft assertion? In python selenium automation.
'''
What is Soft Assertion in Selenium?
->>Soft assertions in Selenium allow a test case to continue executing even after an assertion fails,
as opposed to hard assertions which will immediately stop the execution of the test when an assertion fails.
At the end of the test, the soft assertion framework will aggregate the results and determine whether the test case
passes or fails based on the collection of all the assertions.

->>This is useful when you want to check multiple conditions within a single test case and collect all the failures,
rather than stopping at the first failed assertion.

Soft Assertions in Python Selenium Automation:-
->>Python does not have a built-in soft assertion mechanism like in some other testing frameworks
(e.g., TestNG in Java). However, you can implement soft assertions in Python by collecting assertion results
throughout the test and marking the test as failed at the end if any assertions failed.

->>One common approach is to use a list to store the assertion results and check this list at the end of the test.
Another approach is to use the assert statements within a custom context manager to aggregate the results.

Example: Implementing Soft Assertions in Python
Here’s a basic implementation of soft assertions in Python using a list to store assertion results:
class SoftAssert:
    def __init__(self):
        self._errors = []

    def assert_equal(self, actual, expected, message=""):
        try:
            assert actual == expected, message or f"Expected {expected}, but got {actual}"
        except AssertionError as e:
            self._errors.append(str(e))

    def assert_true(self, condition, message=""):
        try:
            assert condition, message or "Condition is not True"
        except AssertionError as e:
            self._errors.append(str(e))

    def assert_false(self, condition, message=""):
        try:
            assert not condition, message or "Condition is not False"
        except AssertionError as e:
            self._errors.append(str(e))

    def verify(self):
        if self._errors:
            raise AssertionError("\n".join(self._errors))


# Usage of SoftAssert in a Selenium Test

from selenium import webdriver
import pytest

def test_multiple_assertions():
    soft_assert = SoftAssert()

    driver = webdriver.Chrome()
    driver.get("https://www.example.com")

    # Soft assertion 1: Check page title
    soft_assert.assert_equal(driver.title, "Example Domain", "Title does not match")

    # Soft assertion 2: Check if a certain element exists
    try:
        element = driver.find_element("xpath", "//h1")
        soft_assert.assert_true(element is not None, "Header element not found")
    except Exception as e:
        soft_assert.assert_true(False, str(e))

    # Continue testing further conditions
    # Example: Check for an incorrect page title to simulate a failure
    soft_assert.assert_equal(driver.title, "Incorrect Title", "Incorrect title test")

    # At the end, verify all assertions
    soft_assert.verify()

    driver.quit()
->>> Explanation of the Soft Assertion Implementation:
SoftAssert Class: This class contains methods for different types of assertions (assert_equal, assert_true, assert_false).
These methods attempt assertions, and if they fail, they capture the error and store it in a list.

assert_equal/assert_true/assert_false: Each assertion method works similarly to regular assertions but catches
exceptions and stores the errors instead of halting execution.

verify Method: After all assertions have been executed, the verify method checks if there are any stored errors.
If there are, it raises an AssertionError containing all the collected error messages, effectively marking the test
as failed.

Usage in Test: The test collects results from multiple assertions throughout its execution. At the end of the test,
the verify() method is called to check if any assertions failed, marking the test as failed if necessary.
'''
# Alternative: Using pytest's Built-in pytest.fail()
'''
If you are using pytest as your testing framework, you can achieve a similar effect with pytest.fail() 
and continue the test execution manually. For example:
import pytest

def test_soft_assertions():
    errors = []

    try:
        assert 1 == 2
    except AssertionError:
        errors.append("Assertion 1 failed")

    try:
        assert 2 == 2
    except AssertionError:
        errors.append("Assertion 2 failed")

    # Continue with more assertions

    if errors:
        pytest.fail("\n".join(errors))
This script aggregates the errors and fails the test at the end if any assertions failed.


'''
#Marking a Test Case as Failed with Soft Assertions
'''
->>To mark the test case as failed when using soft assertions, you ensure that the verify() method or equivalent 
logic is called at the end of the test. If any soft assertions failed, you can raise an exception 
(such as AssertionError or pytest.fail()) which will signal the test framework that the test has failed.

Summary:-
->Soft Assertions: Allow the test to continue running after an assertion fails, collecting all assertion results.
->Implementation: Use a custom class or a list to collect assertion results and check them at the end of the test.
->Mark Test as Failed: If any assertions fail, raise an exception like AssertionError or use pytest.fail() to mark the test as failed.

Note:- This pattern helps you maintain the flexibility of continuing tests even when some conditions fail, while still ensuring the test is appropriately marked as failed at the end.
'''
