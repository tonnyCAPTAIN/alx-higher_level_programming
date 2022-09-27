#!/usr/bin/python3
"""appending a string at the end of a text file
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """append text to filename"""

    with open(filename, 'r+') as f:
        count = 0
        f = f.write(text)
        for i in text:
            count += 1

        return count
