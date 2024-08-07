from lib.greet import *

def test_greet():
    result = greet("Khari")
    assert result == "Hello, Khari"