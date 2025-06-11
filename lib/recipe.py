
def to_do_checker(text):
    if text  == "":
        raise Exception('No text input')
    elif text == "#TODO":
        return True
