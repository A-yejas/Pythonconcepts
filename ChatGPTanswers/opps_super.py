'''
In Python, the `super()` function is used to call methods from a parent class in a child class.
It's commonly used in the context of inheritance to ensure that the parent class's methods or constructors are
correctly invoked.

### `super()` Method
When we talk about the `super()` method, we're referring to the ability to call a method in a parent class
from within a child class. This is useful for extending or modifying the behavior of inherited methods.

Example:

```python
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()  # Calls the greet method from Parent class
        print("Hello from Child")

obj = Child()
obj.greet()
```

Output:
```
Hello from Parent
Hello from Child
```

### `super()` Constructor
When we refer to the `super()` constructor, we're talking about using `super()`
to call the constructor (`__init__`) of a parent class from a child class.
This ensures that the parent class is properly initialized before or after the child class does its own initialization.

Example:

```python
class Parent:
    def __init__(self, name):
        self.name = name
        print(f"Parent initialized with name: {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Calls the constructor of Parent
        self.age = age
        print(f"Child initialized with age: {self.age}")

obj = Child("Alice", 30)
```

Output:
```
Parent initialized with name: Alice
Child initialized with age: 30
```

### Key Differences
- **Purpose**: `super()` in a method calls a method from the parent class, while `super()` in a constructor calls
the parent class's constructor (`__init__` method).
- **Usage**: The `super()` method is typically used in methods to extend or modify the behavior of inherited methods,
while `super()` in the constructor is used to ensure that the parent class is properly initialized.
- **Context**: Both are often used in classes that inherit from other classes, but `super()`
in constructors is particularly important when the parent class's initialization logic needs to be preserved or
complemented.


'''
