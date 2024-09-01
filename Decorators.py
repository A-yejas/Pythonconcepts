'''
Since allows the programmer to modify the behaviour of functions or class.
Decorators allow us to wrap another function in order to extend the behaviour of wrapped function,
without permanently modifying it.

In decorator, function are taken as the argument into another function and then called inside the function.
--
>>>>>>>>>>>#Decorator to add corresponding elements of two lists
# def add_elements_decorator(func):
#     def wrapper(a, b):
#         # Perform element-wise addition inside the decorator
#         return [a[i] + b[i] for i in range(len(a))]
#     return wrapper
#
# @add_elements_decorator
# def add_lists(a, b):
#     return a, b  # The actual function doesn't do the adding; the decorator does.
# # Example input
# a = [1, 2, 3]
# b = [4, 5, 6]
#
# # Call the function
# result = add_lists(a, b)
# print(result)  # Outputs: [5, 7, 9]


'''
