#!/usr/bin/python3
"""
Module with matrix_divided function
"""


def text_indentation(text):
    """
    Prints text provided but new lines at certain characters.
    :param text: text provided.
    :return: nothing.
    :raises: TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    char = ['.', '?', ':']
    result = ""
    for i in text:
        result += i
        if i in char:
            result += '\n\n'

    lines = result.split('\n')
    formatted_lines = [line.strip() for line in lines]
    formatted_text = '\n'.join(formatted_lines)
    print(formatted_text)
