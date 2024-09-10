# How to find the broken links in selenium with simple examples


'''
You can find broken links on a webpage using
-->Using Selenium in Python by making HTTP requests to the URLs
of all links on the page. A broken link typically returns a status code like 404 (Not Found).
Below is a simple example using Selenium and the `requests` library to check for broken links:

### Prerequisites
- Install the necessary libraries:
  ```bash
  pip install selenium requests
  ```

### Example Code

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

# Initialize the WebDriver (assuming you're using Chrome)
driver = webdriver.Chrome()

# Open the webpage you want to test
driver.get("https://example.com")

# Find all link elements (a tags)
links = driver.find_elements(By.TAG_NAME, "a")

# Loop through the links and check their status
for link in links:
    url = link.get_attribute("href")

    if url is not None:
        try:
            response = requests.head(url)
            if response.status_code >= 400:
                print(f"Broken link: {url} (Status code: {response.status_code})")
            else:
                print(f"Valid link: {url} (Status code: {response.status_code})")
        except requests.exceptions.RequestException as e:
            print(f"Error: {url} ({e})")
    else:
        print("Found a link with no href attribute")

# Close the WebDriver
driver.quit()
```

### Explanation
1. **Set Up WebDriver**: The example assumes you're using Chrome. You might need to download the
appropriate WebDriver and ensure it is in your system's PATH.

2. **Get Links**: The script finds all the `<a>` tags on the webpage.

3. **Check Each Link**: It iterates over each link, extracts the `href` attribute, and sends a
`HEAD` request to the URL using the `requests` library.

4. **Identify Broken Links**: If the response status code is 400 or higher, it's considered a broken link.

5. **Error Handling**: Any exceptions raised during the request (like network issues) are caught and printed.

6. **Close the Browser**: Finally, the browser is closed.

This script provides a simple and straightforward way to find broken links on a webpage using Selenium.
'''
# ------------------POM
'''
The **Page Object Model (POM)** is a design pattern commonly used in Selenium test automation to improve test maintenance and reduce code duplication. In this model, each web page or web component is represented by a corresponding class. The elements on the page are encapsulated within these classes, and methods are created to interact with these elements.

### Example of Page Object Model in Python with Selenium

#### Project Structure
Let's assume you have a simple website with a login page and a dashboard. Your project structure might look like this:

```
my_test_project/
│
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   └── dashboard_page.py
│
├── tests/
│   ├── __init__.py
│   └── test_login.py
│
├── conftest.py
└── requirements.txt
```

#### Step 1: Create the Page Classes

##### `login_page.py`

```python
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "loginBtn")

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()
```

##### `dashboard_page.py`

```python
from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.welcome_message = (By.ID, "welcomeMsg")

    def get_welcome_message(self):
        return self.driver.find_element(*self.welcome_message).text
```

#### Step 2: Create Test Cases

##### `test_login.py`

```python
import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_valid_login(driver):
    driver.get("https://example.com/login")

    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)

    # Perform login
    login_page.enter_username("testuser")
    login_page.enter_password("password123")
    login_page.click_login()

    # Verify successful login by checking the welcome message
    welcome_message = dashboard_page.get_welcome_message()
    assert welcome_message == "Welcome, testuser!"
```

#### Step 3: Configure Fixtures

##### `conftest.py`
This file is used for setting up and tearing down the WebDriver instance, which will be shared across multiple test files.

```python
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Initialize the WebDriver (e.g., Chrome)
    driver = webdriver.Chrome()

    # Yield the WebDriver to the test
    yield driver

    # Close the browser after the test is completed
    driver.quit()
```

#### Step 4: Run the Tests

To run your tests, navigate to your project directory and execute:

```bash
pytest tests/
```

### Explanation

- **Page Classes**: The `LoginPage` and `DashboardPage` classes represent the login page and the dashboard page, 
respectively. These classes encapsulate the elements of the pages and provide methods to interact with them.

- **Tests**: The `test_login.py` file contains a test that verifies whether a user can log in successfully. 
It uses the methods defined in the page classes to perform actions and assertions.

- **Fixtures**: The `conftest.py` file contains the setup for the WebDriver, ensuring that a new browser 
instance is started before each test and closed afterward.

### Advantages of POM

- **Reusability**: The page classes can be reused across different test cases.
- **Maintenance**: If the page layout changes, only the corresponding page class needs to be updated, not all the 
test cases.
- **Readability**: Tests become more readable and focused on the actions being performed rather than on the details 
of how to interact with the page.

This is a simple example of how you can implement the Page Object Model in Python using Selenium. 
You can expand it by adding more complex interactions, handling dynamic elements, and incorporating additional 
design patterns like the Factory Pattern or Singleton Pattern as needed.

'''
##>>Factory in pom selenium automation python
'''
The **Factory Pattern** in the Page Object Model (POM) is a design pattern that provides an efficient way to create instances of page objects. By using a factory, you can centralize the creation of page objects and make your tests cleaner and more maintainable.

### Why Use a Factory Pattern in POM?
- **Centralized Object Creation**: It provides a single place for managing the creation of page objects, reducing redundancy.
- **Flexibility**: If the way a page object is instantiated changes, you only need to update the factory, not every test.
- **Simplifies Tests**: Tests focus on the actions and assertions rather than object creation.

### Implementing the Factory Pattern in POM

Let's expand on the previous example where we had a `LoginPage` and a `DashboardPage`. We will now implement a factory to handle the creation of these page objects.

#### Step 1: Define Page Classes

These classes remain the same as in the previous example. Here they are for reference:

##### `login_page.py`

```python
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "loginBtn")

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()
```

##### `dashboard_page.py`

```python
from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.welcome_message = (By.ID, "welcomeMsg")

    def get_welcome_message(self):
        return self.driver.find_element(*self.welcome_message).text
```

#### Step 2: Implement the Factory

The factory will manage the instantiation of page objects.

##### `page_factory.py`

```python
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

class PageFactory:
    def __init__(self, driver):
        self.driver = driver

    def get_page(self, page_name):
        if page_name.lower() == "login":
            return LoginPage(self.driver)
        elif page_name.lower() == "dashboard":
            return DashboardPage(self.driver)
        else:
            raise ValueError(f"Unknown page: {page_name}")
```

#### Step 3: Update the Tests to Use the Factory

In the test, we now use the `PageFactory` to create instances of page objects.

##### `test_login.py`

```python
import pytest
from page_factory import PageFactory

def test_valid_login(driver):
    driver.get("https://example.com/login")

    factory = PageFactory(driver)

    # Get the LoginPage using the factory
    login_page = factory.get_page("login")
    dashboard_page = factory.get_page("dashboard")

    # Perform login
    login_page.enter_username("testuser")
    login_page.enter_password("password123")
    login_page.click_login()

    # Verify successful login by checking the welcome message
    welcome_message = dashboard_page.get_welcome_message()
    assert welcome_message == "Welcome, testuser!"
```

#### Step 4: Use Fixtures to Handle WebDriver Setup

This remains the same as before, where you define your WebDriver setup in `conftest.py`.

##### `conftest.py`

```python
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
```

#### Step 5: Run the Tests

Execute the tests as usual:

```bash
pytest tests/
```

### Explanation

- **PageFactory Class**: The `PageFactory` class takes the WebDriver instance and provides a method `get_page()` to instantiate the correct page object based on the provided page name.

- **Factory Usage in Tests**: In `test_login.py`, instead of directly creating instances of `LoginPage` and `DashboardPage`, we use the factory to get these instances. This reduces the dependency on specific page class imports and centralizes the creation logic.

- **Flexibility and Maintenance**: If you ever need to change how the page objects are created (e.g., passing additional parameters), you only need to update the factory, making your tests more maintainable and flexible.

### Advantages of Using Factory in POM

1. **Centralized Control**: The factory pattern centralizes control over the instantiation of page objects, leading to easier management.
2. **Reduced Coupling**: Tests are less tightly coupled to the specific classes they use, allowing for easier updates or refactoring.
3. **Cleaner Tests**: Tests focus on interactions and validations rather than the mechanics of object creation, leading to cleaner and more readable test code.

This pattern is particularly useful in larger test suites where multiple page objects are involved, and object creation logic might become complex.

'''
#SHALLOW COPY & DEEP COPY
'''
### Shallow Copy vs. Deep Copy in Python

When you copy an object in Python, there are two types of copies you can make: a **shallow copy** and a **deep copy**. 
Understanding the difference between these two is crucial when dealing with complex data structures 
like nested lists or dictionaries.

#### Shallow Copy

A **shallow copy** creates a new object, but it inserts references to the objects found in the original. 
If the original object contains nested objects (like lists within lists), the shallow copy will contain references 
to the same nested objects.

##### Example of Shallow Copy

```python
import copy

# Original list with nested list
original_list = [1, 2, [3, 4]]

# Create a shallow copy of the list
shallow_copy_list = copy.copy(original_list)

# Modify the nested list in the original
original_list[2][0] = 99

print("Original List:", original_list)  # Output: [1, 2, [99, 4]]
print("Shallow Copy List:", shallow_copy_list)  # Output: [1, 2, [99, 4]]
```

**Explanation:**
- The `shallow_copy_list` is a new list, but it references the same inner list `[3, 4]` as the `original_list`.
- When you modify the inner list in the `original_list`, the change is reflected in the `shallow_copy_list` as well, 
because they both reference the same inner list.

#### Deep Copy

A **deep copy** creates a new object and recursively copies all objects found within the original, creating completely independent objects. Any changes made to the original or the copied object do not affect each other.

##### Example of Deep Copy

```python
import copy

# Original list with nested list
original_list = [1, 2, [3, 4]]

# Create a deep copy of the list
deep_copy_list = copy.deepcopy(original_list)

# Modify the nested list in the original
original_list[2][0] = 99

print("Original List:", original_list)  # Output: [1, 2, [99, 4]]
print("Deep Copy List:", deep_copy_list)  # Output: [1, 2, [3, 4]]
```

**Explanation:**
- The `deep_copy_list` is a completely independent copy of the `original_list`.
- Changes made to the `original_list`, such as modifying the inner list, do not affect the `deep_copy_list`.

### Summary

- **Shallow Copy**: Creates a new object, but does not create copies of objects within the original. If the original contains other objects (like lists within a list), the shallow copy will reference the same objects as the original.
- **Deep Copy**: Creates a completely independent copy of the original object and all nested objects. Changes in the original or the copy do not affect each other.

Use shallow copy when you want to create a new object but don't mind if the nested objects are shared between the original and the copy. Use deep copy when you need an entirely independent copy, especially when dealing with complex, nested data structures.

'''
# --->>>>>>>>>>>>>>>>>>>
