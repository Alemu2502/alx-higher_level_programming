#!/usr/bin/python3
# 5-no_c.py
# Kobo Highschool <375@kobohighschool.com>


def no_c(my_string):
    """Replace all characters c and c from a string."""
    copy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(copy))
