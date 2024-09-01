from selenium import webdriver
from selenium.webdriver.common.by import By

class BrowserAutomation:
    def __init__(self, driver_path, browser='chrome'):
        # Initialize the browser driver (e.g., Chrome or Firefox)
        if browser == 'chrome':
            self.driver = webdriver.Chrome(executable_path=driver_path)
        elif browser == 'firefox':
            self.driver = webdriver.Firefox(executable_path=driver_path)
        else:
            raise ValueError("Unsupported browser! Please use 'chrome' or 'firefox'.")

    def open_browser(self, url):
        # Open the browser and navigate to the specified URL
        self.driver.get(url)
        self.driver.maximize_window()

    def verify_title(self, expected_title):
        # Verify the title of the webpage
        actual_title = self.driver.title
        if actual_title == expected_title:
            print(f"Title verification successful: '{actual_title}'")
        else:
            print(f"Title verification failed: Expected '{expected_title}', but got '{actual_title}'")

    def close_browser(self):
        # Close the browser
        self.driver.quit()

# Example usage:
if __name__ == "__main__":
    driver_path = "/path/to/your/chromedriver"  # Update this to your actual driver path
    url = "https://www.example.com"
    expected_title = "Example Domain"

    # Initialize the BrowserAutomation class
    browser_automation = BrowserAutomation(driver_path=driver_path, browser='chrome')

    # Open the browser and navigate to the URL
    browser_automation.open_browser(url)

    # Verify the title of the webpage
    browser_automation.verify_title(expected_title)

    # Close the browser
    browser_automation.close_browser()
'''
Below is an example of a Python class that uses Selenium WebDriver to open a browser, navigate to a specific URL, 
and verify the title of the webpage.

### Explanation:

1. **`__init__(self, driver_path, browser='chrome')`**: 
   - The constructor initializes the WebDriver based on the specified browser (either Chrome or Firefox).
   - The `driver_path` argument specifies the path to the WebDriver executable (e.g., `chromedriver`).

2. **`open_browser(self, url)`**: 
   - This method opens the browser, navigates to the provided URL, and maximizes the window.

3. **`verify_title(self, expected_title)`**: 
   - This method retrieves the title of the current webpage and compares it to the `expected_title`. It prints whether the title matches or not.

4. **`close_browser(self)`**: 
   - This method closes the browser window and ends the WebDriver session.

### Usage:

- Update the `driver_path` to point to your `chromedriver` or `geckodriver` executable.
- Update the `url` to the website you want to test.
- Provide the expected title of the webpage for comparison.

Let me know if you need further enhancements to this example!
'''
