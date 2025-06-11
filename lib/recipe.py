
def to_do_checker(text):
    if text  == "":
        raise Exception('No text input')
    elif "#TODO" in text:
        return True
    return False

# method that checks for #TODO, and something else
