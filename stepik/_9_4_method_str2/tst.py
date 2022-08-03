def first_word(text: str) -> str:
    """
    returns the first word in a given text.
    """
    # your code here
    text = 'asdas dfdgdf '
    prob = text.find(' ')
    return text[0:prob]
