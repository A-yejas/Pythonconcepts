'''
lambda:- lambda is another way to create a function,
lambda is one line anonymous function it doesnt contains name.
Using lambda we can do only one expression
example:- lambda arguments: expression
# Define a lambda function to add two numbers
add = lambda x, y: x + y

# Use the lambda function
result = add(3, 5)
print(result)  # Output: 8
print(lambda x,y:x+y,3,5)

'''


# add = lambda x, y: x + y
#
# # Use the lambda function
# result = add(3, 5)
# print(result)  # Output: 8
# # print(lambda x,y:x+y,3,5)
a = 1
b = 3

# Define a lambda function to multiply two numbers
multiply = ((lambda x, y: x * y)(a,b))

# Call the lambda function with the integers
result = multiply
print(result)  # Output: 3
# -----------------------
'''
Map is used to do operations on each iyerable value and it will return the all operarions result in map object
format.
Map takes 2 parameters one is function another one is iterable object.
Example:- map(function, iterable)
# Define a function to square a number
def square(x):
    return x * x

# Use map() to apply the function to each item in the list
numbers = [1, 2, 3, 4]
squared_numbers = map(square, numbers)

# Convert the map object to a list and print it
print(list(squared_numbers))  # Output: [1, 4, 9, 16]

'''
###################
'''
Zip() is used to map the similar index of multiple containers and return as zip object.
or
zip function is defined as Zip(*iterator) the function takes iterables as argument and return an iterator.
This iterator generate a series of tuples containing elements from each iterable.
Zip() function can accept the any type of iterables.eg: list.
ex:-zip(iterable1, iterable2, ...)

a=[1,2,3,4,5]
b=['a','b','c','d']
print(list(zip(a,b)))
---------------------
# Define two lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# Use zip() to combine the lists
combined = zip(names, ages)

# Convert the zip object to a list and print it
print(list(combined))  # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

'''
##########################
'''
Reduce:- Is used to operations on each iterable value and return all operations result as sum.
Reduce takes 2 parameters one is function another one is iterable object.
# from functools import reduce

# reduce(function, iterable, [initializer])
def fun(x,y):
    return x+y
nus=[1,2,3,4]
res =reduce(fun, nus)
print(res)
'''
############################
'''
Filter method is used filters the given sequence with the help of filter function and return filter object.
Filter takes 2 parameters one is function and another one is iterable object.
filter(function, iterable)
# Define a function to check if a number is even
def is_even(x):
    return x % 2 == 0

# Use filter() to apply the function to each item in the list
numbers = [1, 2, 3, 4, 5]
even_numbers = filter(is_even, numbers)

# Convert the filter object to a list and print it
print(list(even_numbers))  # Output: [2, 4]
 
'''

