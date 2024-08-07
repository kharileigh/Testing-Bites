from lib.string_builder import *

def test_string_builder():
    builder = StringBuilder()
    builder.add("Love is..")
    builder.size()
    assert builder.output() == "Love is.."