from lib.gratitudes import *

def test_add():

    #initiate Class
    gratitudes = Gratitudes()
    gratitudes.add("life")
    #in class, contructor creates a list -- assertion must show it is added to a list
    assert gratitudes.gratitudes == ["life"]

def test_format():

    #initiate Class
    gratitudes = Gratitudes()
    #add a gratitude to then use to format
    gratitudes.add("life")
    #format gratitude taking expected result from function
    assert gratitudes.format() == "Be grateful for: life"
