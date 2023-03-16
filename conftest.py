import pytest 

class User:

        def __init__(self, age) -> None:
                self.age = age
        def remove(self):
                self.age = None

@pytest.fixture(scope="function")
def user():
        # before test
        print("Create user")
        user = User(42)

        # pass user object to test
        yield user

        # after test
        print("remove user")
        user.remove()