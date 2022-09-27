#!/usr/bin/python3
"""appending a string at the end of a text file
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """append text to filename"""

    with open(filename, 'W') as f:
        count = 0
        j = f.write(text)
        last_line = j.readline()[-1]
        for i in last_line:
            count += 1

        return count
