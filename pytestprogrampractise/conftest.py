import pytest


@pytest.fixture(autouse=True,scope='class')
def setup_data():
    # Setup code (e.g., initializing a variable or opening a file)
    data = {"name": "pytest", "type": "framework"}
    print("SetUP>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    yield
    print("TEAR DOWN ><><><><<><><???????????????????")
    return data
