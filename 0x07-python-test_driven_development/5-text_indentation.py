#!/usr/bin/python3
""" text_indentation function
"""

'''
File_name: 5-text_indentation.py
Created: 3rd of June, 2023
Auth: David James Taiye (Official0mega)
Size: undefined
Project: 0x07-python-test_driven_development
Status: submitted.
'''


def text_indentation(text):
    """
    # Write a function that prints a text with 2 new lines after each of....
    # ...these characters: ., ? and :
    # text must be a string, otherwise raise a TypeError exception with....
    # ....the message text must be a string....
    # There should be no space at the beginning or at the end of...
    # ...each printed line....
    # VARIABLE(" "):
    # text_indentation(Str): Text indentation
    # Return: Always 0, (Success).

    Prints a text with 2 new lines after each '.', '?', and ':' character.

    Args:
        matrix (list): The matrix to be divided. Must be a matrix
        ...text (str): The text to be indented. ....

    Raises:
        ...TypeError: If text is not a string. Example....

    Example:
    ext_indentation("Hello. This is a sample text. How are you?")
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    else:
        res = []
        a = 0
        text_len = len(text)
        skip_spaces = True
        is_end = False
        is_delim = False
        for i in range(text_len):
            is_end = i == text_len - 1
            is_delim = text[i] in '.?:'
            if is_delim or is_end:
                res.append(text[a: i + 1] + ('\n\n' * is_delim))
                skip_spaces = True
                a = i + 1
            elif text[i] in ' \t\r\v' and skip_spaces:
                a += 1
            elif text[i] == '\n':
                res.append(text[a: i + 1].rstrip() + '\n')
                a += 1
                skip_spaces = True
            else:
                if skip_spaces:
                    a = i
                skip_spaces = False
        print(''.join(res), end='')
