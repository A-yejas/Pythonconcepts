'''
Python functions are blocks of reusable code that perform a specific task. They help in organizing and
structuring code, making it more readable and maintainable. Here's a rundown of Python functions:

### Basic Syntax

```python
def function_name(parameters):
    # Function body
    return value
```

### Key Concepts

1. **Defining a Function**
   Use the `def` keyword to define a function, followed by the function name and parentheses that may include parameters.

   ```python
   def greet(name):
       return f"Hello, {name}!"
   ```

2. **Calling a Function**
   Call a function by using its name followed by parentheses. Pass arguments inside the parentheses if needed.

   ```python
   print(greet("Alice"))  # Outputs: Hello, Alice!
   ```

3. **Parameters and Arguments**
   - **Parameters**: Variables listed inside the parentheses in the function definition.
   - **Arguments**: Actual values passed to the function when calling it.

   ```python
   def add(a, b):  # a and b are parameters
       return a + b

   result = add(3, 4)  # 3 and 4 are arguments
   ```

4. **Default Parameters**
   You can provide default values for parameters. If the argument is not provided, the default value is used.

   ```python
   def power(base, exponent=2):
       return base ** exponent

   print(power(3))        # Uses default exponent 2, outputs: 9
   print(power(3, 3))     # Uses provided exponent 3, outputs: 27
   ```

5. **Keyword Arguments**
   You can pass arguments by specifying the parameter name.

   ```python
   def describe_person(name, age):
       return f"{name} is {age} years old."

   print(describe_person(age=30, name="Bob"))  # Outputs: Bob is 30 years old.
   ```

6. **Variable-Length Arguments**
   You can use `*args` and `**kwargs` to handle variable numbers of arguments.

   - **`*args`**: For non-keyword arguments.
     ```python
     def concatenate(*args):
         return " ".join(args)

     print(concatenate("Hello", "world", "from", "Python"))  # Outputs: Hello world from Python
     ```

   - **`**kwargs`**: For keyword arguments.
     ```python
     def print_info(**kwargs):
         for key, value in kwargs.items():
             print(f"{key}: {value}")

     print_info(name="Alice", age=30, city="New York")
     # Outputs:
     # name: Alice
     # age: 30
     # city: New York
     ```

7. **Return Values**
   Functions can return values using the `return` statement. If no `return` statement is used,
   `None` is returned by default.

   ```python
   def square(x):
       return x * x

   result = square(5)  # result will be 25
   ```

8. **Lambda Functions**
   Anonymous functions defined with the `lambda` keyword. They are typically used for short, throwaway functions.

   ```python
   add = lambda x, y: x + y
   print(add(5, 7))  # Outputs: 12
   ```

### Example

Here's a complete example that includes different types of parameters and variable-length arguments:

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

def calculate_sum(*args):
    return sum(args)

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Function calls
print(greet("Alice"))  # Outputs: Hello, Alice!
print(greet("Bob", "Hi"))  # Outputs: Hi, Bob!

print(calculate_sum(1, 2, 3, 4, 5))  # Outputs: 15

print_info(name="Charlie", age=25, profession="Engineer")
# Outputs:
# name: Charlie
# age: 25
# profession: Engineer
```

Functions are a fundamental aspect of Python and play a crucial role in writing clean and efficient code.

'''
