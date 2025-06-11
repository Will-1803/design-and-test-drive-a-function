from lib.recipe import *
import pytest

"""
Given an empty string, return an error  
"""
def test_to_do_checker_string_no_empty():
    with pytest.raises(Exception) as e:
        to_do_checker("")
    actual = str(e.value)
    assert actual == "No text input"



# """
# Given a string that contains #TODO, return true

# """
# to_do_checker("#TODO") => True

def test_given_TODO():
    result = to_do_checker('#TODO')
    assert result == True



# """
# Given a string that contains #todo in lower case 
# """

def test_given_TODO():
    result = to_do_checker('#todo')
    assert result == False


# """
# Given a string that does not contain #TODO return False
# """
# to_do_checker("GO TO THE SHOP") => False

# """