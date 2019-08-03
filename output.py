# Author: Alex J Davies (alexjdavies.net

"""
Holds functions used for outputting text.
TODO: refactor functions from handler.py and parsing.py
"""


def vprint(verbose, string):
    if verbose is True:
        print(string)
