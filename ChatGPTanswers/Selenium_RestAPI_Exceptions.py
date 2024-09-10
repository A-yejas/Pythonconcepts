'''
In Selenium WebDriver, exceptions are used to handle errors that occur during the execution of your test scripts.
Properly handling these exceptions is crucial for making your test scripts robust and reliable.
Below is an overview of some common Selenium WebDriver exceptions and how to handle them in Python with examples.
--------------------------------
1. NoSuchElementException :---
Occurs When: The WebDriver is unable to find an element using the provided locator.
How to Handle: Use try-except block to catch the exception and handle it gracefully.
ORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR

NoSuchElementException: This exception is thrown when an element with given attributes is not found on the web page
'''

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get('https://example.com')
    element = driver.find_element(By.ID,'non_existent_id')
except NoSuchElementException:
    print("Element not found")

driver.quit()
'''
TimeoutException
Occurs When: A command in your script exceeds the time limit before completion, such as a wait command. 
How to Handle: You can catch this exception and either retry the operation or log the error.
OOOOOOOOOOOOOOOOOOOOOORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
TimeoutException: This exception is thrown when a command performing an operation does not complete in the stipulated 
time

'''
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get('https://example.com')
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'some_id'))
    )
except TimeoutException:
    print("Element took too long to load")

driver.quit()
'''
ElementNotVisibleException
Occurs When: The element is present in the DOM but not visible on the page. How to Handle: 
Check the visibility of the element before interacting with it.
ORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
ElementNotVisibleException: This exception is thrown when the element is present in DOM (Document Object Model), 
but not visible on the web page
'''
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException

driver = webdriver.Chrome()

try:
    driver.get('https://example.com')
    element = driver.find_element(By.ID,'hidden_element_id')
    element.click()
except ElementNotVisibleException:
    print("Element is not visible")

driver.quit()
'''
ElementNotInteractableException:--
Occurs When: The element is visible but not interactable (e.g., disabled). 
How to Handle: Check if the element is interactable before performing actions.

'''
from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException

driver = webdriver.Chrome()

try:
    driver.get('https://example.com')
    element = driver.find_element(By.ID, 'disabled_element_id')
    element.click()
except ElementNotInteractableException:
    print("Element is not interactable")

driver.quit()
'''
StaleElementReferenceException:-
Occurs When: The referenced element is no longer attached to the DOM. How to Handle: Refresh the reference 
to the element.
ORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
StaleElementException: This exception is thrown when the element is either deleted or no longer attached to the DOM

'''
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException

driver = webdriver.Chrome()

try:
    driver.get('https://example.com')
    element = driver.find_element(By.ID,'some_id')
    driver.refresh()  # Refreshing the page causes a stale element reference
    element.click()  # This will throw StaleElementReferenceException
except StaleElementReferenceException:
    element = driver.find_element(By.ID,'some_id')  # Re-find the element
    element.click()

driver.quit()
'''
InvalidSelectorException
Occurs When: The selector used to locate an element is invalid or not recognized.
How to Handle: Correct the selector or use a different locating strategy.

'''
from selenium import webdriver
from selenium.common.exceptions import InvalidSelectorException

driver = webdriver.Chrome()

try:
    driver.get('https://example.com')
    element = driver.find_element(By.ID,'//[@id="some_id"]')  # Invalid XPath
except InvalidSelectorException:
    print("Invalid selector used")

driver.quit()
'''
WebDriverException
Occurs When: There’s an issue with the WebDriver itself, such as being unable to initiate a session or locate the browser. 
How to Handle: Retry starting the WebDriver or provide an alternative WebDriver.
'''
##Handling Exceptions in REST API Testing
'''
In REST API testing using Python, exceptions are commonly related to network issues, invalid responses, 
or errors in the API request itself. Here’s how to handle some common exceptions:

ConnectionError Occurs When: There’s a problem with the network connection or server.
'''
import requests

try:
    response = requests.get('https://api.example.com/data')
    response.raise_for_status()  # Raise an HTTPError for bad responses
except requests.exceptions.ConnectionError:
    print("Failed to connect to the server")
'''
Timeout Occurs When: The request takes too long to complete. Example:
'''
import requests

try:
    response = requests.get('https://api.example.com/data', timeout=5)
except requests.exceptions.Timeout:
    print("The request timed out")
'''
HTTPError Occurs When: The server returns an unsuccessful status code. Example:
'''
import requests

try:
    response = requests.get('https://api.example.com/data')
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
'''
Best Practices for Exception Handling
Graceful Degradation: Provide alternative workflows or meaningful messages instead of letting the script crash.
Logging: Log exceptions to a file for debugging purposes.
Retry Mechanism: Implement retry logic for recoverable exceptions like TimeoutException.
Custom Exceptions: Create custom exceptions for more granular control.
By understanding and correctly handling these exceptions, you can build more robust and reliable test automation 
scripts using Selenium WebDriver and REST API testing in Python.
'''
