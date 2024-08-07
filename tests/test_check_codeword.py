from lib.check_codeword import *

# check if condition is met
def test_check_codeword():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

# check elif condition is met
def test_check_codeword_close():
    result = check_codeword("haze")
    assert result == "Close, but nope."

# check else condition is met
def test_check_codeword_wrong():
    result = check_codeword("car")
    assert result == "WRONG!"