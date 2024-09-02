#Fixture scopes
'''
In the context of automated testing using Python's pytest framework, fixtures are functions that are used to
set up preconditions (like setting up test data, initializing a database, or preparing some configuration) and
clean up afterward. Fixtures can have scopes, which determine how long the fixture is active and when it is invoked.

->>>>>>>>>Fixture Scopes
pytest provides four types of fixture scopes
1.function Scope (default):

The fixture is created and destroyed for each test function or method that uses it.
This is the most common scope and is used when you need a fresh setup for every test.
-----

@pytest.fixture
def setup_function():
    # Setup code here
    yield
    # Teardown code here
'''
#class Scope:
'''
The fixture is created once per class. All the test methods within that class will use the same instance of the fixture.
Useful when the setup is costly and can be reused across multiple methods in a class.
------------
@pytest.fixture(scope="class")
def setup_class():
    # Setup code here
    yield
    # Teardown code here
'''
#module Scope:
'''
#->>The fixture is created once per module (i.e., per Python file). All test functions and methods 
within the same module will share the same fixture instance.
->>This scope is useful when you have shared setup code for all tests in a module.

@pytest.fixture(scope="module")
def setup_module():
    # Setup code here
    yield
    # Teardown code here

'''
#session Scope:
'''
->>The fixture is created once for the entire test session, and it is shared across all tests that use it.
->>This is typically used when setting up something that is expensive and only needs to be done once, 
like a database connection that can be reused by all tests in the session.
------
@pytest.fixture(scope="session")
def setup_session():
    # Setup code here
    yield
    # Teardown code here


'''
# Example of Fixture Scopes
'''
import pytest

# Fixture with function scope (default)
@pytest.fixture
def setup_function():
    print("\nSetup for each function")
    yield
    print("\nTeardown for each function")

# Fixture with class scope
@pytest.fixture(scope="class")
def setup_class():
    print("\nSetup for each class")
    yield
    print("\nTeardown for each class")

# Fixture with module scope
@pytest.fixture(scope="module")
def setup_module():
    print("\nSetup for the module")
    yield
    print("\nTeardown for the module")

# Fixture with session scope
@pytest.fixture(scope="session")
def setup_session():
    print("\nSetup for the session")
    yield
    print("\nTeardown for the session")



'''
#Practical Use Cases
'''
Function Scope: Use this when every test needs a fresh setup and teardown. For example, 
if you're testing CRUD operations and want to reset data after each test, use function scope.

Class Scope: Use this when you want to initialize some shared state for a group of tests within a class, 
such as preparing data that multiple test methods will modify.

Module Scope: Use this when multiple test functions across the same module need the same shared state or resources, 
like a shared fixture across different test classes in the same file.

Session Scope: Use this for expensive or heavy setup/teardown, such as setting up a database connection 
that can be reused across all tests.
-------------------------------------------------------
############-->>>>>>>>>>>Choosing the Right Scope
The scope of your fixture depends on how often the fixture setup needs to be recreated and how it impacts the tests:

Use function scope if you need isolation between tests.
Use class, module, or session scopes for shared setup across multiple tests when it's costly to recreate for each test.

'''
# 2/SEP/2024
'''
### **What are Fixtures in Pytest?**

Fixtures in pytest are functions used to set up some preconditions or a specific state before the actual tests 
run and tear down the state after the tests have been executed. They help in writing cleaner and more maintainable 
test code by reducing redundancy. Fixtures can be shared across multiple tests, making them reusable and efficient.

### **Where Are Fixtures Used?**
Fixtures are commonly used in scenarios where you need:
- **Setup and Teardown:** Preparing the environment before tests (e.g., launching a browser) and cleaning up 
afterward (e.g., closing the browser).
- **Dependency Injection:** Providing data or objects that tests depend on (e.g., a database connection, 
configuration files, etc.).
- **Test Isolation:** Ensuring that tests do not affect each other by resetting states between tests.

### **Types of Fixtures**

1. **Module-level Fixtures:**
   - Scope: `module`
   - Usage: Set up resources that are required for the entire module.
   - Example: Initializing a database connection used by all tests in a module.

2. **Function-level Fixtures:**
   - Scope: `function`
   - Usage: Set up resources needed for individual test functions.
   - Example: Opening and closing a browser for each test function.

3. **Class-level Fixtures:**
   - Scope: `class`
   - Usage: Set up resources required for all tests in a class.
   - Example: Creating a test client for web testing.

4. **Session-level Fixtures:**
   - Scope: `session`
   - Usage: Set up resources that should persist for the duration of the test session.
   - Example: Starting a Selenium Grid or a Docker container at the start of a test session and 
   stopping it at the end.

### **Fixture Methods**
- **`@pytest.fixture`**: The basic decorator used to define a fixture.
- **`scope`**: Defines the scope of the fixture. Possible values are `function`, `class`, `module`, and `session`.
- **`autouse`**: If set to `True`, the fixture is automatically used by all tests without needing to be 
explicitly called.
- **`yield`**: Can be used to define setup and teardown logic within a single fixture function.

### **Custom Fixtures in Python Selenium Automation**

#### **Example: Browser Setup and Teardown using Fixtures**

Let's create a custom fixture that opens a browser before each test and closes it afterward.

**Step 1: Define the Fixture**

```python
import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    # Setup: Start the browser before each test
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # Teardown: Close the browser after each test
    driver.quit()
```

**Step 2: Use the Fixture in Your Test**

```python
class TestGoogleSearch:
    
    def test_open_google(self, browser):
        browser.get("https://www.google.com")
        assert "Google" in browser.title
    
    def test_search_python(self, browser):
        browser.get("https://www.google.com")
        search_box = browser.find_element_by_name("q")
        search_box.send_keys("Python")
        search_box.submit()
        assert "Python" in browser.title
```

### **Explanation:**
- **Fixture `browser`:** 
  - This fixture sets up the browser using Selenium's `webdriver.Chrome()` before each test and ensures 
  it’s closed after the test using `driver.quit()`. The `yield` statement allows the test function to run in 
  between the setup and teardown.
  - The `scope="function"` indicates that the browser setup and teardown will occur for each individual test function.

- **Using the Fixture in Tests:**
  - The fixture is passed as an argument to the test methods `test_open_google` and `test_search_python`. 
  Pytest automatically injects the fixture into the test functions when they are called.

### **Benefits of Using Fixtures:**
- **Reusability:** You can use the `browser` fixture in multiple test cases without duplicating setup and teardown code.
- **Modularity:** Fixtures can be shared across different test modules or even projects.
- **Maintenance:** If you need to change the setup process (e.g., switching from Chrome to Firefox), you only 
need to update the fixture, not every test case.

### **Conclusion:**
Fixtures in pytest are powerful tools that help streamline the testing process by managing setup and teardown, 
injecting dependencies, and isolating test environments. Custom fixtures are particularly useful in Selenium automation,
 where you often need to manage browser instances and test data efficiently.

'''
# ----------------------------------------------------------------AUTO USE:----------------
'''
In pytest, the `autouse` parameter in a fixture determines whether the fixture should be automatically 
applied to all tests within its scope, without the need to explicitly declare the fixture in the test function's 
argument list.

### **What Does `autouse=True` Mean?**

When you set `autouse=True` in a fixture, the fixture will be automatically invoked for every test that falls 
within the fixture's scope (function, class, module, or session) without you having to pass it explicitly in the 
test functions.

### **When to Use `autouse=True`:**
- **Global Setup/Teardown:** When you want to apply certain setup or teardown steps to every test 
function or class without explicitly passing the fixture to each test.
- **Side Effects:** When the fixture performs actions like logging, setting up a test environment, 
or cleaning up resources that are needed by every test.
- **Consistency:** When you want to ensure that certain conditions or states are always met for every test.

### **Example:**

Let’s look at an example where you want to ensure that the database is cleared before each test runs, 
without needing to explicitly call the fixture in each test function.

```python
import pytest

@pytest.fixture(scope="function", autouse=True)
def clear_database():
    # Imagine this function clears the database
    print("Clearing the database...")
    # You could also add actual code to reset the state of the database here.

def test_add_user():
    print("Test adding a user")
    assert True

def test_delete_user():
    print("Test deleting a user")
    assert True
```

### **Explanation:**

- **`clear_database` Fixture:**
  - The fixture is defined with `autouse=True`, which means it will automatically run before 
  each test function within its scope (`function` in this case).
  - Every time a test function runs, you’ll see the message "Clearing the database…" 
  printed, indicating that the database clearing process is being applied before each test.

- **Test Functions:**
  - The test functions `test_add_user` and `test_delete_user` don’t need to explicitly call the 
  `clear_database` fixture. The fixture is applied automatically due to `autouse=True`.

### **Output When Running the Tests:**
```
Clearing the database...
Test adding a user
Clearing the database...
Test deleting a user
```

This demonstrates that the `clear_database` fixture was executed before each test function, 
ensuring that the database is cleared before each test runs.

### **When Not to Use `autouse=True`:**
- **Overuse:** If a fixture is not needed for every single test, it’s better to not use `autouse=True` to avoid 
unnecessary overhead.
- **Explicit Dependencies:** When you want to make it clear in the test function which fixtures are being used, 
it’s better to explicitly pass them as arguments instead of relying on `autouse=True`.

In summary, `autouse=True` is useful for fixtures that should always be applied automatically across tests within 
their scope, ensuring certain setup or teardown actions are consistently executed.

'''
