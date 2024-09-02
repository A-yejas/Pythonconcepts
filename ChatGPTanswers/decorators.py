# Q:-use of decorators in python explain with simple understanding examples
'''
Decorators in Python are a way to modify or enhance the behavior of functions or methods without
changing their actual code. They allow you to wrap a function with another function, adding functionality
before or after the wrapped function runs.

### Basic Concept
Imagine you have a function that does something simple, like printing a message. Now, what if you want to log
that this function was called every time it runs? You could add logging code to the function, but that would mix
concerns (logging with the actual functionality). Instead, you can use a decorator to add the logging separately.

### How Decorators Work
A decorator is a function that takes another function as an argument, adds some functionality,
and then returns a new function.

### Example 1: A Simple Decorator

Here’s a basic example to illustrate:

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_hello():
    print("Hello!")

# Applying the decorator manually
decorated_function = my_decorator(say_hello)
decorated_function()
```

**Output:**
```
Something is happening before the function is called.
Hello!
Something is happening after the function is called.
```

In this example:
1. `my_decorator` is a decorator function.
2. `say_hello` is the function being decorated.
3. The `wrapper` function adds extra functionality before and after calling `func()`
(which is `say_hello` in this case).

### Example 2: Using the `@` Syntax

In Python, you can apply a decorator using the `@` symbol, which is a shorthand:

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

**Output:**
```
Something is happening before the function is called.
Hello!
Something is happening after the function is called.
```

By using the `@my_decorator` syntax, Python automatically applies `my_decorator` to the `say_hello` function.

### Example 3: Decorator with Arguments

Decorators can also take arguments. Here's an example:

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()
```

**Output:**
```
Hello!
Hello!
Hello!
```

In this case:
1. `repeat` is a decorator factory that takes an argument `n`.
2. It returns a `decorator` function that, when applied, calls the original function `n` times.

### Summary
- **Decorators** are functions that modify the behavior of other functions.
- They help keep your code clean by separating concerns (e.g., logging, access control, etc.).
- You can apply decorators using the `@decorator_name` syntax.
- Decorators can also take arguments to create more dynamic behavior.

'''
##########func() means in above code
'''
In the examples provided, `func()` refers to the original function that is being passed into the decorator.

Here's a breakdown of what it does:

### Inside the Decorator

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper
```

- `func` is a parameter of the `my_decorator` function. It represents the function that is being decorated.
- When `func()` is called within the `wrapper` function, it actually calls the original function that was passed to the decorator.

### Example Walkthrough

If we have:

```python
@my_decorator
def say_hello():
    print("Hello!")
```

- The `say_hello` function is passed to `my_decorator` as the `func` argument.
- The decorator returns the `wrapper` function, which now becomes the new `say_hello` function.
- When you call `say_hello()`, it actually calls `wrapper()`.
- Inside `wrapper`, calling `func()` triggers the original `say_hello()` function, so `Hello!` is printed.

To summarize:
- `func` is the original function that the decorator is modifying.
- `func()` is the actual call to that original function within the decorator.
'''
