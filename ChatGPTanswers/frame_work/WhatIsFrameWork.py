#what is framework in simple terms
'''
1.frame work is like set of tools, guidelens and structures that help you build somthing easily and efficiently
'''
#Explain Pytest Framework
'''
1.Pytest framework is designed to make it eazy to write to small,scalable test cases.
2.Pytest is a flexible and easy-to-use for writing and running tests in Python.
3.It offers helpful feature  fixtures, parameterization, assertions, and plugins.
4.Commonly used in both web automation and API automation
'''
#Key Features of pytest Framework:
'''
1.Easy to write tests, Tests can be written with simple Python functions.
2.pytest automatically discovers/recognize test files and test functions following/bases on specific naming conventions 
(e.g., files starting with test_ or ending with _test).
3.Fixtures:  
1.Fixtures make it easy to reuse (setup) code across multiple tests! For example we have setup & Teardown methods.
(e.g., setting up database connections, browser sessions).
ORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
Fixtures are a key feature that helps you set up some conditions before tests run and clean up afterward. 
They are particularly useful for setting up test environments such as opening a browser for web automation or connecting
to a database.
###################################<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
Parameterization: Easily test the same functionality with multiple sets of data.
<><><><><><><><><><><><><><><><><><><><><><><><>ORRRRR<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
Parameterization allows you to run the same test function with different sets of input data. This is useful for 
testing multiple scenarios.
#####################
Assertions with Useful Output: pytest provides better error messages compared to standard assert statements, making it 
easier to debug.
###########################################
Plugins and Extensions: A rich ecosystem of plugins (e.g., for parallel test execution, coverage reports) can extend 
pytest's functionality.
><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><
######################################################
><><><><><><><><><><><><><><><><><>Running Specific Tests:><><><><><><><><><><><><><><><><><>
You can run specific tests by:

Test name: pytest test_sample.py::test_addition
#################################### GENERATE TESTS REPORTS:><><><><><><><><><><><><><><><><><>
You can generate test reports with pytest. One common plugin for reports is pytest-html, 
which creates an HTML report of the test results.
pytest --html=report.html
###############
Common Plugins for pytest:
pytest-xdist: For running tests in parallel.
pytest-cov: For generating code coverage reports.
pytest-html: For generating HTML reports.
><><><><><><><><><><><><><><><><><>#####################################################################
conftest.py: This file is used to define shared fixtures across multiple test files. 
It is placed in the root or subdirectories to make fixtures accessible within that scope.
#####################################################################################
Configuration (pytest.ini):
You can define settings for pytest using a pytest.ini file in the root of your project. 
It helps configure logging, markers, and other test settings.


'''
import pytest

@pytest.mark.parametrize("x, y, expected", [(1, 2, 3), (2, 3, 5), (3, 4, 7)])
def test_add(x, y, expected):
    assert x + y == expected
    print(">>>>>>>>",x)
    print(x + y)
###################################
import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    # Setup browser
    driver = webdriver.Chrome()
    yield driver
    # Quit browser
    driver.quit()

def test_google_search(browser):
    # Open Google
    browser.get("https://www.google.com")
    # Check title contains 'Google'
    assert "Google" in browser.title


