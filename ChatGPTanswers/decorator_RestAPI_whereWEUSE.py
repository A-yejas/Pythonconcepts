'''
Here’s a detailed breakdown of each point:

### 1. **Use of Decorators in Python Selenium Automation and Python REST API Automation**
   - **Python Selenium Automation:**
     - Decorators are often used to wrap functions that interact with web elements. For instance, a retry mechanism
     can be implemented with a decorator to handle intermittent failures when interacting with web elements.
     - Example: A decorator to automatically retry finding a stale element.
     ```python
     from selenium.common.exceptions import StaleElementReferenceException

     def retry_on_stale_element(func):
         def wrapper(*args, **kwargs):
             for _ in range(3):  # Retry up to 3 times
                 try:
                     return func(*args, **kwargs)
                 except StaleElementReferenceException:
                     continue
             raise StaleElementReferenceException("Element is not stable")
         return wrapper
     ```
     - **Python REST API Automation:**
       - Decorators can be used to manage preconditions or postconditions around API calls, like authentication,
       logging, or retrying failed requests.
       - Example: A decorator to add headers for authentication.
       ```python
       def add_auth_headers(func):
           def wrapper(*args, **kwargs):
               headers = kwargs.get('headers', {})
               headers['Authorization'] = 'Bearer YOUR_TOKEN'
               kwargs['headers'] = headers
               return func(*args, **kwargs)
           return wrapper
       ```

### 2. **Use of Constructor in Python Selenium Automation and Python REST API Automation**
   - **Python Selenium Automation:**
     - Constructors are typically used in Page Object Models (POM) to initialize the web driver and elements of the page.
     - Example:
     ```python
     class LoginPage:
         def __init__(self, driver):
             self.driver = driver
             self.username_field = driver.find_element(By.ID, 'username')
             self.password_field = driver.find_element(By.ID, 'password')
             self.login_button = driver.find_element(By.ID, 'login')
     ```
   - **Python REST API Automation:**
     - Constructors can be used to initialize base URLs, authentication tokens, or other configurations.
     - Example:
     ```python
     class APIClient:
         def __init__(self, base_url, token):
             self.base_url = base_url
             self.headers = {'Authorization': f'Bearer {token}'}
     ```

### 3. **How to Handle Stale Element Exceptions**
   - **StaleElementReferenceException** occurs when the web element you’re trying to interact with is no longer attached
    to the DOM. To handle this:
     - **Retry Mechanism**: Implement a retry loop to re-find the element when this exception occurs.
     - **Explicit Waits**: Use WebDriverWait with conditions like `element_to_be_clickable` or `presence_of_element_located`.
     - **Example**:
     ```python
     from selenium.webdriver.common.by import By
     from selenium.webdriver.support.ui import WebDriverWait
     from selenium.webdriver.support import expected_conditions as EC
     from selenium.common.exceptions import StaleElementReferenceException

     element = WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((By.ID, 'some_id'))
     )

     for i in range(3):  # Retry mechanism
         try:
             element.click()
             break
         except StaleElementReferenceException:
             element = driver.find_element(By.ID, 'some_id')
     ```

### 4. **How to Run the Same Code in Two Different Environments at the Same Time**
   - **Parallel Execution**: You can use tools like `pytest-xdist` for parallel execution across different environments.
   - **Separate Configuration Files**: Maintain separate configuration files for different environments and pass
   the environment as a parameter.
   - **Example**:
     - Run tests with different configurations:
     ```bash
     pytest -n 2 --env=prod --env=staging
     ```
     - Use `pytest-xdist` for parallel execution:
     ```bash
     pytest -n 2
     ```

### 5. **Types of Exceptions in Selenium**
   - **NoSuchElementException**: Thrown when an element could not be found.
   - **TimeoutException**: Thrown when a command does not complete in the specified time.
   - **StaleElementReferenceException**: Thrown when an element is no longer attached to the DOM.
   - **ElementNotInteractableException**: Thrown when an element is not interactable.
   - **InvalidElementStateException**: Thrown when an element is in a state where the desired action cannot be performed.
   - **WebDriverException**: Thrown when the WebDriver is unable to perform an action.
   - **NoAlertPresentException**: Thrown when an attempt is made to switch to an alert, but no alert is present.

### 6. **Important Points in Pytest and Plugins for Python Selenium and REST API Automation**
   - **pytest-xdist**: For parallel test execution.
   - **pytest-html**: For generating HTML reports.
   - **pytest-cov**: For measuring test coverage.
   - **pytest-mock**: For mocking during tests.
   - **pytest-asyncio**: For testing asynchronous code.
   - **Usage in Selenium**: Use these plugins to parallelize tests, generate reports, and check coverage.
   - **Usage in REST API**: Same plugins can be applied to run API tests, check coverage, and generate detailed reports.

### 7. **REST API Status Codes and When They Occur**
   - **1xx (Informational)**: The request was received, continuing the process.
   - **2xx (Success)**
     - **200 OK**: The request was successful.
     - **201 Created**: The request was successful and a new resource was created.
     - **204 No Content**: The request was successful but there is no content to send in the response.
   - **3xx (Redirection)**
     - **301 Moved Permanently**: The resource has been moved to a new URL permanently.
     - **302 Found**: The resource is temporarily available at a different URL.
     - **304 Not Modified**: The resource has not been modified since the last request.
   - **4xx (Client Error)**
     - **400 Bad Request**: The request could not be understood or was missing required parameters.
     - **401 Unauthorized**: Authentication failed or user does not have permissions for the desired action.
     - **403 Forbidden**: Authentication succeeded but authenticated user does not have access to the resource.
     - **404 Not Found**: The requested resource could not be found.
     - **409 Conflict**: A request conflict with the current state of the server.
   - **5xx (Server Error)**
     - **500 Internal Server Error**: A generic error occurred on the server.
     - **502 Bad Gateway**: The server was acting as a gateway or proxy and received an invalid response.
     - **503 Service Unavailable**: The server is currently unable to handle the request due to a temporary
     overload or maintenance.

These concepts are key in both Selenium and API automation, providing a strong foundation for managing test
execution, error handling, and parallel testing.

'''
###############
'''
Decorators in Python are powerful tools that allow you to modify the behavior of a function or a method. 
In Selenium automation and REST API automation, decorators can be particularly useful for repetitive tasks like logging,
 retrying operations, or adding common functionality (e.g., authentication headers) to multiple functions.

### **Example in Python Selenium Automation**

#### **Use Case: Handling StaleElementReferenceException with a Decorator**
When interacting with web elements, you may encounter a `StaleElementReferenceException`, which occurs when the DOM 
has been updated and the reference to the web element is no longer valid. You can use a decorator to automatically 
retry the interaction when this exception occurs.

**Decorator Implementation:**
```python
from selenium.common.exceptions import StaleElementReferenceException

def retry_on_stale_element(max_retries=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except StaleElementReferenceException as e:
                    print(f"Attempt {attempt + 1} failed due to stale element. Retrying...")
            raise StaleElementReferenceException(f"Element is still stale after {max_retries} attempts")
        return wrapper
    return decorator
```

**Usage in Selenium Test:**
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = driver.find_element(By.ID, 'username')
        self.password_field = driver.find_element(By.ID, 'password')
        self.login_button = driver.find_element(By.ID, 'login')

    @retry_on_stale_element(max_retries=3)
    def enter_username(self, username):
        self.username_field.send_keys(username)

    @retry_on_stale_element(max_retries=3)
    def click_login(self):
        self.login_button.click()

# Example usage
driver = webdriver.Chrome()
login_page = LoginPage(driver)
login_page.enter_username("testuser")
login_page.click_login()
```
In this example, the `retry_on_stale_element` decorator automatically retries the `enter_username` and `click_login` 
methods up to 3 times if a `StaleElementReferenceException` is encountered. This ensures that your test is more robust
 and less likely to fail due to transient DOM updates.

### **Example in Python REST API Automation**

#### **Use Case: Adding Authentication Headers to API Requests**
When working with REST APIs, you might need to add authentication headers to every request. Instead of manually 
adding the headers in each API call, you can create a decorator to handle this.

**Decorator Implementation:**
```python
def add_auth_headers(func):
    def wrapper(*args, **kwargs):
        headers = kwargs.get('headers', {})
        headers['Authorization'] = 'Bearer YOUR_ACCESS_TOKEN'
        kwargs['headers'] = headers
        return func(*args, **kwargs)
    return wrapper
```

**Usage in REST API Test:**
```python
import requests

class APIClient:
    BASE_URL = "https://api.example.com"

    @add_auth_headers
    def get_user_details(self, user_id, headers=None):
        url = f"{self.BASE_URL}/users/{user_id}"
        response = requests.get(url, headers=headers)
        return response.json()

# Example usage
client = APIClient()
user_details = client.get_user_details(user_id=123)
print(user_details)
```

In this example, the `add_auth_headers` decorator automatically adds an `Authorization` header to the 
`get_user_details` method. This way, you don’t need to worry about manually adding the authentication token every 
time you make a request, reducing redundancy and potential errors.

### **Summary**
- **Selenium Automation:** Use decorators like `retry_on_stale_element` to automatically handle exceptions and retry 
operations, making your tests more resilient.
- **REST API Automation:** Use decorators like `add_auth_headers` to inject common headers or 
perform common pre-processing tasks for your API requests, simplifying your code and making it easier to maintain.

These examples illustrate how decorators can help streamline repetitive tasks and enhance the robustness of your
 automation frameworks.


'''
