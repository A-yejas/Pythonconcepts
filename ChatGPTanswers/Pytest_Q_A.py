'''
->For someone with 5 years of experience in automation testing using `pytest`,
interview questions are likely to explore both your practical experience and your
understanding of more advanced features. Below are some common questions along with suggested answers:

### 1. **What is `pytest` and why do you prefer it over other testing frameworks?**
   - **Answer**: `pytest` is a testing framework for Python that allows you to write simple as well as scalable test cases.
   I prefer `pytest` because of its simplicity in writing tests, the rich set of plugins available, and its powerful
   features like fixtures, parameterization, and its ability to run tests in parallel with the `pytest-xdist` plugin.
   Additionally, its detailed failure reports and flexible assertion introspection make debugging easier.

### 2. **Can you explain what a `pytest` fixture is and give an example of how you've used one?**
   - **Answer**: A `pytest` fixture is a function used to provide setup code that is automatically invoked before your
   test functions run. For example, I often use fixtures to set up a WebDriver instance for browser automation tests.
   Here’s a simple example:
     ```python
     @pytest.fixture
     def setup_browser():
         driver = webdriver.Chrome()
         driver.maximize_window()
         yield driver
         driver.quit()
     ```
     In my tests, I then use this fixture by simply adding it as an argument to the test functions,
     allowing for reusable setup and teardown code.

### 3. **What is the purpose of the `autouse=True` argument in `pytest` fixtures?**
   - **Answer**: The `autouse=True` argument in a `pytest` fixture automatically applies the fixture to
   all test functions in the scope without needing to explicitly include it as an argument in each test function.
   I use `autouse=True` when I want certain setup or teardown code to run for every test function in the module or class,
   such as initializing a database connection or cleaning up data before each test.

### 4. **How do you run tests in parallel using `pytest`?**
   - **Answer**: To run tests in parallel using `pytest`, I use the `pytest-xdist` plugin, specifically the `-n` option.
   For instance, running `pytest -n 4` will distribute the tests across 4 cores, executing them in parallel.
   This is particularly useful for reducing the overall test execution time in large test suites.

### 5. **How do you handle dependencies between tests in `pytest`?**
   - **Answer**: In `pytest`, tests are ideally independent, but if there’s a need to share data or state between tests,
   I use fixtures to manage the shared setup. Additionally, if tests must run in a particular order due to dependencies,
   `pytest` allows for the use of the `pytest-dependency` plugin. However, I prefer designing my tests to be independent
   wherever possible to avoid order-dependent issues.

### 6. **What is parameterization in `pytest` and how have you used it?**
   - **Answer**: Parameterization in `pytest` allows you to run the same test with different inputs.
   This is done using the `@pytest.mark.parametrize` decorator. I often use parameterization to test different data sets
   or input values without writing multiple test functions. Here’s a simple example:
   ----------
     ```python
     @pytest.mark.parametrize("username, password", [
         ("user1", "pass1"),
         ("user2", "pass2"),
         ("user3", "pass3"),
     ])
     def test_login(username, password):
         assert login(username, password) == "Success"
     ```
     This approach increases test coverage while keeping the code concise.

### 7. **How do you skip or mark a test as expected to fail in `pytest`?**
   - **Answer**: To skip a test, I use the `@pytest.mark.skip` decorator or `@pytest.mark.skipif` for conditional skipping.
   For marking a test as expected to fail, I use the `@pytest.mark.xfail` decorator.
   These are useful when dealing with known issues or when a test is not relevant for certain conditions.
     - Example:
       ```python
       @pytest.mark.skip(reason="Skipping this test temporarily")
       def test_temporary_skip():
           assert 1 == 1

       @pytest.mark.xfail(reason="Known bug in function X")
       def test_known_bug():
           assert some_function() == expected_result
       ```

### 8. **Explain the use of `conftest.py` in `pytest`.**
   - **Answer**: The `conftest.py` file in `pytest` is used for sharing fixtures, hooks, and other configurations
   across multiple test files. It is automatically discovered by `pytest` and can be placed at various directory
   levels to control the scope of the fixtures it provides. This is useful in large projects where fixtures need to be
   reused across different test modules or packages.

### 9. **What are pytest hooks and how have you used them?**
   - **Answer**: `pytest` hooks are functions that allow you to insert custom logic at specific points in the
    testing process, such as before a test starts, after a test finishes, or when a test fails. For example,
    I have used the `pytest_runtest_setup` hook to perform certain checks before a test is executed,
    like ensuring required environment variables are set.

### 10. **How do you integrate `pytest` with CI/CD pipelines?**
    - **Answer**: Integrating `pytest` with CI/CD pipelines involves configuring the pipeline
    (e.g., Jenkins, GitLab CI, or GitHub Actions) to run `pytest` commands during the build or deployment process.
    This typically includes running tests, collecting coverage reports with `pytest-cov`, and generating test reports
    in formats like JUnit XML for better integration with CI/CD tools. This ensures that tests are automatically
    run on every code change, providing continuous feedback on the code quality.

### 11. **How do you capture and manage logs in `pytest`?**
    - **Answer**: `pytest` has built-in logging capabilities that can capture logs during test execution.
    I use the `caplog` fixture to capture and assert logs within a test. Additionally, I configure logging settings in
    the `pytest.ini` file or directly in the test script to manage log levels, log formatting, and log file outputs.

### 12. **How do you manage test dependencies in `pytest`?**
    - **Answer**: To manage test dependencies, I primarily use fixtures and careful test design to ensure that
     each test is as independent as possible. When dependencies are unavoidable, I use the `pytest-dependency`
      plugin to indicate dependencies between tests. However, my goal is always to keep tests independent to allow
      for parallel execution and reduce the chance of cascading failures.

These questions and answers should provide a solid foundation for a discussion during an interview for a role involving
 `pytest` in automation testing, especially for someone with around 5 years of experience.
'''

