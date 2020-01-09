import pytest

@pytest.yield_fixture()
def setUp():
    print("Once before every method")
    yield
    print("Once after every method")

def test_method_A(setUp):
    print("Running method A")

def test_method_B(setUp):
    print("Running method B")