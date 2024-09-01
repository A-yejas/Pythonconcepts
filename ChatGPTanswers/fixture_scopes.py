#Fixture scopes
'''
In the context of automated testing using Python's pytest framework, fixtures are functions that are used to
set up preconditions (like setting up test data, initializing a database, or preparing some configuration) and
clean up afterward. Fixtures can have scopes, which determine how long the fixture is active and when it is invoked.

->>>>>>>>>Fixture Scopes
pytest provides four types of fixture scopes
1.function Scope (default):

The fixture is created and destroyed for each test function or method that uses it.
This is the most common scope and is used when you need a fresh setup for every test.
-----

@pytest.fixture
def setup_function():
    # Setup code here
    yield
    # Teardown code here
'''
#class Scope:
'''
The fixture is created once per class. All the test methods within that class will use the same instance of the fixture.
Useful when the setup is costly and can be reused across multiple methods in a class.
------------
@pytest.fixture(scope="class")
def setup_class():
    # Setup code here
    yield
    # Teardown code here
'''
#module Scope:
'''
#->>The fixture is created once per module (i.e., per Python file). All test functions and methods 
within the same module will share the same fixture instance.
->>This scope is useful when you have shared setup code for all tests in a module.

@pytest.fixture(scope="module")
def setup_module():
    # Setup code here
    yield
    # Teardown code here

'''
#session Scope:
'''
->>The fixture is created once for the entire test session, and it is shared across all tests that use it.
->>This is typically used when setting up something that is expensive and only needs to be done once, 
like a database connection that can be reused by all tests in the session.
------
@pytest.fixture(scope="session")
def setup_session():
    # Setup code here
    yield
    # Teardown code here


'''
# Example of Fixture Scopes
'''
import pytest

# Fixture with function scope (default)
@pytest.fixture
def setup_function():
    print("\nSetup for each function")
    yield
    print("\nTeardown for each function")

# Fixture with class scope
@pytest.fixture(scope="class")
def setup_class():
    print("\nSetup for each class")
    yield
    print("\nTeardown for each class")

# Fixture with module scope
@pytest.fixture(scope="module")
def setup_module():
    print("\nSetup for the module")
    yield
    print("\nTeardown for the module")

# Fixture with session scope
@pytest.fixture(scope="session")
def setup_session():
    print("\nSetup for the session")
    yield
    print("\nTeardown for the session")



'''
#Practical Use Cases
'''
Function Scope: Use this when every test needs a fresh setup and teardown. For example, 
if you're testing CRUD operations and want to reset data after each test, use function scope.

Class Scope: Use this when you want to initialize some shared state for a group of tests within a class, 
such as preparing data that multiple test methods will modify.

Module Scope: Use this when multiple test functions across the same module need the same shared state or resources, 
like a shared fixture across different test classes in the same file.

Session Scope: Use this for expensive or heavy setup/teardown, such as setting up a database connection 
that can be reused across all tests.
-------------------------------------------------------
############-->>>>>>>>>>>Choosing the Right Scope
The scope of your fixture depends on how often the fixture setup needs to be recreated and how it impacts the tests:

Use function scope if you need isolation between tests.
Use class, module, or session scopes for shared setup across multiple tests when it's costly to recreate for each test.

'''

