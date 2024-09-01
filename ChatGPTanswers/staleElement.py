'''
Stale element exception

A "Stale Element Reference Exception" typically occurs in Selenium when you try to interact with an element
that is no longer part of the DOM or has been refreshed or removed from it. This usually happens when the DOM
has changed between the time you located the element and the time you tried to interact with it.

### Common Scenarios:
1. **Page Reload or Navigation:** The page reloads or navigates to another page after you locate an element
but before you perform an action on it.
2. **Dynamic Content:** The element is part of a dynamic UI where content is added or removed, causing the DOM to change.
3. **AJAX Calls:** An AJAX request updates the page's DOM, causing the element reference to become stale.

### How to Handle It:
1. **Relocate the Element:** Before interacting with the element, try to find it again.
    ```python
    element = driver.find_element(By.ID, "your-element-id")
    element.click()
    ```

2. **Use `WebDriverWait`:** Explicitly wait until the element is present and ready for interaction.
    ```python
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "your-element-id"))
    )
    element.click()
    ```

3. **Try-Catch Block:** Implement a try-catch block to catch the exception and re-locate the element.
    ```python
    try:
        element = driver.find_element(By.ID, "your-element-id")
        element.click()
    except StaleElementReferenceException:
        element = driver.find_element(By.ID, "your-element-id")
        element.click()
    ```

4. **Check for Dynamic Changes:** If you suspect the DOM changes are causing the issue,
try to identify what triggers these changes (e.g., an AJAX call) and wait for the changes to complete.

By re-locating the element or waiting explicitly for it, you can often avoid encountering a
"Stale Element Reference Exception."


'''
