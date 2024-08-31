'''
1.List Comprehensions:- List comprehension is allow you  to create new list by applying the expression on each item
in an existing iterable. ex:- [expression for item in iterable if condition]

# Create a list of squares for numbers 0 to 9
squares = [x**2 for x in range(10)]
print(squares)
ANS:- [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
-----------------------
2. Set Comprehensions:- Set comprehession are similar to list comprehenssion but creates a set instead of list.
Since do not allow duplicate values , is any duplicate value is removed automatically.
{expression for item in iterable if condition}
ex:- # Create a set of unique squares for numbers 0 to 9
unique_squares = {x**2 for x in range(10)}
print(unique_squares)
AND:- {0, 1, 64, 4, 36, 9, 16, 81, 49, 25}
-----------------------
-3.Dictionary Comprehensions:- Dictionary comprehensions allow you to create a dictionary by applying an
expression to each item in an existing iterable, where each element becomes a key-value pair.
ex:- {key_expression: value_expression for item in iterable if condition}
# Create a dictionary where the keys are numbers 0 to 9 and the values are their squares
square_dict = {x: x**2 for x in range(10)}
print(square_dict)
ANS:- {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
----
4.Generator Comprehensions
Generator comprehensions are similar to list comprehensions, but instead of creating a list,
they create a generator object, which yields items one at a time. This is more memory-efficient for large datasets.
ex:- (expression for item in iterable if condition)
# Create a generator for squares of numbers 0 to 9
squares_gen = (x**2 for x in range(10))

# To access the items, you can iterate over the generator
for square in squares_gen:
    print(square)
ANS:-
0
1
4
9
16
25
36
49
64
81
-----------------
'''

from selenium import webdriver

# A generator that yields a series of URLs to test
def url_generator():
    base_url = "http://example.com/"
    for i in range(1, 6):
        yield f"{base_url}{i}"

# Set up the Selenium WebDriver (assuming you have the correct driver installed)
driver = webdriver.Chrome()

# Iterate over the URLs using the generator
for url in url_generator():
    driver.get(url)
    print(f"Testing {url}")
    # Add your assertions or checks here, e.g., checking the page title or elements
    assert "Expected Title" in driver.title

# Quit the WebDriver
driver.quit()

