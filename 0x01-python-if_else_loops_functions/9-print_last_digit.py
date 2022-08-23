#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        lastDigit = number % 10
    else:
        lastDigit = number % -10
        lastDigit *= -1

    print("{:d}".format(lastDigit), end='')
    return (lastDigit)
