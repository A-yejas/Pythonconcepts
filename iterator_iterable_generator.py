# iterator:- Using iterators are can get the sequence of values based on demamd bu using next() methoc
'''
The iter() function is used to create an iterator from an iterable, and the
next() function is used to retrieve the next element from the iterator.
1.iter(numbers) creates an iterator object from the list numbers.
2.next(numbers_iter) retrieves the next item from the iterator. Each time you call next(),
it returns the next element in the sequence.
**If you call next() after all elements have been returned, Python raises a StopIteration exception,
indicating that there are no more items to return.

Benfits:-
Memory Efficiency: Iterators are useful when dealing with large datasets because they don’t load all elements
into memory at once; they generate each element only when needed.
Lazy Evaluation: Iterators allow for lazy evaluation, which means you can process large streams of data or
infinite sequences efficiently.
Below is the example:-
'''
l=[1,2,34]
iter_obj=iter(l)
print(next(iter_obj))
# or
for i in iter_obj:
    print('>>>',i)
#we can get sequence of values based on loop function
'''
Iterables:- 
An iterable in python is any object capble of returning its members one at a time.
Examples of iterables include lists, tuples, strings, and dictionaries

Benefits of Using Iterables:
1.Easy Looping: Iterables allow you to loop through data structures in a simple and readable way.
2.Compatibility with Iterators: You can easily convert an iterable into an iterator using iter() 
if you need more control over the iteration process.
3.Wide Range of Applicability: Since most data structures in Python are iterables, 
you can use the same looping techniques across different types of collections.

'''
# Create a list of fruits
fruits = ["apple", "banana", "cherry"]

# Use a for loop to iterate over the list
for fruit in fruits:
    print(fruit)
#Generator we can execute a block of code based on demand using next() function.Using Yield keyword we can create a generator.
'''
Generator:- Generator we can execute a block of code based on demand using next() function.
Using Yield keyword we can create a generator.
Benefits of Using Generators in Selenium Testing:-
1.Lazy Evaluation: Only the current URL is generated and processed, which saves memory.
2.Simplified Code: Generators allow for cleaner and more maintainable code, especially when 
dealing with large datasets or complex sequences.
3.Flexibility: You can easily modify the generator to produce different sequences of URLs 
based on various conditions or parameters.
'''
# from selenium import webdriver
#
# # A generator that yields a series of URLs to test
# def url_generator():
#     base_url = "http://example.com/page"
#     for i in range(1, 6):
#         return f"{base_url}{i}"
#
# # Set up the Selenium WebDriver (assuming you have the correct driver installed)
# driver = webdriver.Chrome()
#
# # Iterate over the URLs using the generator
# for url in url_generator():
#     driver.get(url)
#     print(f"Testing {url}")
#     # Add your assertions or checks here, e.g., checking the page title or elements
#     assert "Expected Title" in driver.title
# # Quit the WebDriver
# driver.quit()
# -------------------
# def generator(n):
#     for i in range(n):
#         print('Before Return')
#         yield i
#         print('After yield')
#         yield i
# n=generator(10)
# # print(list(n))
# print((next(n)))
# print((next(n)))
# print((next(n)))
# for j in n:
#     print('for loop', j)
# print('>>>>>>>>>>>')
# def generator(n):
#     print('Frst return')
#     yield 9
#     print('Second return')
#     yield 5

