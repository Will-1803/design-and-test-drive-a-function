# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user

So that I can find my tasks among all my notes

I want to check if a line from my notes includes the string `#TODO`.

We want a string that contains #TODO in full caps to return true 
string that not contains #TODO to return false

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def to_do_checker(text):
    #Parameters, One parameter that conatins a line from the users notes.

    #Returns a boolean. True if contains #TODO or False if not. 

    # Side effects: none, 

        pass # Test-driving means _not_ writing any code here yet.

```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE
"""
Given an empty string, return an error  
"""
extract_uppercase("") => "no info given"

"""
Given a string that contains #TODO, return true

"""
to_do_checker("#TODO") => True

"""
Given a string that contains #todo in lower case 
"""
to_do_checker("#todo") => False

"""
Given a string that does not contain #TODO return False
"""
to_do_checker("GO TO THE SHOP") => False

"""
Given a lower and a mixed case word
It returns an empty list
"""
extract_uppercase("hello WoRLD") => []

"""
Given a lowercase word and an uppercase word with an exclamation mark
It returns a list with the uppercase word, no exclamation mark
"""
extract_uppercase("hello WORLD!") => ["WORLD"]

"""
Given an empty string
It returns an empty list
"""
extract_uppercase("") => []

"""
Given a None value
It throws an error
"""
extract_uppercase(None) throws an error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
