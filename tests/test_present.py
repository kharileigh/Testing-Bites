# pytest - has an utility to handle exceptions so must import
import pytest
from lib.present import *


"""""
---------- wrap an item
---------- get it back when unwrapping
"""
def test_wrap_and_then_unwrap():
    present = Present()
    present.wrap(33)
    assert present.unwrap() == 33


"""
---------- unwrap before wrapping
"""
def test_unwrap_without_wrapping():
    present = Present()
    with pytest.raises(Exception) as err:
        present.unwrap()
    error_message = str(err.value)
    assert error_message == "No contents have been wrapped."


""""
--------- wrap already wrapped present
"""
def test_wrap_already_wrapped():

    present = Present()

    # - wrap present first
    present.wrap(66)

    # wrap line of code that generates exception error - caught here
    with pytest.raises(Exception) as err:

        # - wrap again to trigger exception
        present.wrap(44)

    # extract exception itself - by putting error in a variable - convert to string to get message 
    error_message = str(err.value)
    
    # assert expected error message
    assert error_message == "A contents has already been wrapped."
    

""""
--------- wrap already - try to wrap again - first value is unchanged
"""
def test_wrapping_already_wrapped_preserves_value():
    present = Present()

    present.wrap(66)

    with pytest.raises(Exception) as err:
        present.wrap(44)
    
    assert present.unwrap() == 66