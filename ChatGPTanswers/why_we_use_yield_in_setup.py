'''
In Selenium Python, the `yield` keyword is used in pytest fixtures to ensure proper setup and teardown of resources,
such as the Selenium WebDriver. When you create a pytest fixture that uses `yield`, it allows the code before `yield`
to set up resources (like launching the browser), and the code after `yield` is executed after the test is completed
(like closing the browser).

Here's why `yield` is useful for closing the driver in Selenium tests:

1. **Resource Management**: `yield` splits the fixture into two phases. The code before `yield` sets up the environment
 (e.g., initializing the WebDriver), and the code after `yield` is executed after the test, allowing you to clean up
 resources (e.g., closing the WebDriver).

2. **Test Completion**: After the test function using the fixture is executed, pytest resumes execution after
the `yield`, so any cleanup tasks (like calling `driver.quit()`) are handled even if the test fails or raises an exception.

3. **Elegant Teardown**: Using `yield` helps to avoid writing separate teardown code. It ensures that the WebDriver
is closed regardless of how the test exits (success, failure, or error).

### Example:

```python
import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    # Setup: Initialize WebDriver
    driver = webdriver.Chrome()
    yield driver  # Hand over control to the test function

    # Teardown: Quit WebDriver after test completion
    driver.quit()

def test_google_search(browser):
    browser.get("https://www.google.com")
    assert "Google" in browser.title
```

In this example:
- The browser is initialized before the `yield`.
- The `yield` gives control to the test function (`test_google_search`).
- After the test completes, the code after `yield` (i.e., `driver.quit()`) is executed to close the browser.

This approach ensures that the WebDriver is properly closed after each test, regardless of whether the test passes or fails.


'''
