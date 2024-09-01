#Can you call the base class method without creating an instance? In python
'''
Yes, you can call a base class method without creating an instance in Python by using the class name
directly along with the method name. However, this only works for class methods and static methods,
not for instance methods, because instance methods require an instance of the class to be called.

Here’s how you can do it:
For a class method:
class Base:
    @classmethod
    def base_class_method(cls):
        print("Base class method called")

# Calling the base class method without creating an instance
Base.base_class_method()
For a static method:
class Base:
    @staticmethod
    def base_static_method():
        print("Base static method called")

# Calling the base static method without creating an instance
Base.base_static_method()
For an instance method:
Instance methods require an instance of the class, so you cannot call them without creating an instance.
class Base:
    def instance_method(self):
        print("Instance method called")

# You need to create an instance to call an instance method
base_instance = Base()
base_instance.instance_method()
Note:- So, you can call class and static methods without creating an instance, but not instance methods.
---------------------
#########What is operator overloading?in python
Operator overloading in Python refers to the ability to define or customize the behavior of standard operators
(like +, -, *, etc.) when they are applied to objects of user-defined classes. This allows objects of these
classes to be used with operators just like built-in types, making the code more intuitive and easier to read.

Python achieves operator overloading by allowing special methods (also known as "magic methods" or "dunder
methods") to be defined in a class. These special methods have double underscores at the beginning and end of
their names and correspond to specific operators.

Example of Operator Overloading
Let's consider a simple example where we define a Point class to represent a point in 2D space.
We'll overload the + operator so that it can add two Point objects together.
#####
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

# Creating two Point objects
p1 = Point(1, 2)
p2 = Point(3, 4)

# Using the overloaded + operator
p3 = p1 + p2

print(p3)  # Output: (4, 6)
Key Points:
__add__ Method: This method is used to define the behavior of the + operator. In the example,
p1 + p2 triggers the __add__ method of the Point class, which adds the x and y coordinates of p1 and p2.

Other Operators: Similar to __add__, there are many other special methods for different operators:

__sub__ for -
__mul__ for *
__truediv__ for /
__eq__ for ==
__lt__ for <
And so on.
Operator overloading allows you to make your custom classes behave more like built-in types,
improving the natural usage of objects in Python.

-----------
1. Public (No Underscore)
Syntax: variable_name or method_name
Description: By default, all members (variables and methods) in a Python class are public.
This means they can be accessed from anywhere, both inside and outside the class.

class MyClass:
    def __init__(self):
        self.public_var = 42

    def public_method(self):
        return "Public method"

obj = MyClass()
print(obj.public_var)  # Accessible
print(obj.public_method())  # Accessible
--------------
2. Protected (Single Underscore)
Syntax: _variable_name or _method_name
Description: By convention, a single leading underscore (_) is used to indicate that a member is intended for
internal use only. It suggests that the member is protected and should not be accessed directly from outside the class.
However, this is only a convention, and the member can still be accessed if needed.

class MyClass:
    def __init__(self):
        self._protected_var = 42

    def _protected_method(self):
        return "Protected method"

obj = MyClass()
print(obj._protected_var)  # Still accessible, but not recommended
print(obj._protected_method())  # Still accessible, but not recommended
3. Private (Double Underscore)
Syntax: __variable_name or __method_name
Description: A double leading underscore (__) triggers name mangling, which makes the member harder
to access from outside the class. Python internally changes the name of the member to include the class name,
effectively making it private. However, it is still technically accessible through name mangling.

class MyClass:
    def __init__(self):
        self.__private_var = 42

    def __private_method(self):
        return "Private method"

obj = MyClass()
# The following will raise an AttributeError:
# print(obj.__private_var)
# print(obj.__private_method())

# Accessing using name mangling:
print(obj._MyClass__private_var)  # Accessible through name mangling
print(obj._MyClass__private_method())  # Accessible through name mangling







'''
