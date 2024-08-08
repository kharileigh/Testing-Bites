import pytest
from lib.password_checker import *


""""
-- assert password meets condition - 8 characters
"""
def test_password_eight():
    checker = PasswordChecker()
    password = checker.check("12345678")
    assert password == True



""""
-- assert password does not meet condition - less than 8
"""
def test_password_less_than_8():
    checker = PasswordChecker()

    # wrap line that raises exception - password less than 8 characters
    with pytest.raises(Exception) as err:
        checker.check("1234")
    
    # extract error message
    error_message = str(err.value)
    assert error_message == "Invalid password, must be 8+ characters."

