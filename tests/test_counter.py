from lib.counter import *

def test_counter():
    counter = Counter()
    counter.add(4)
    assert counter.report() == "Counted to 4 so far."