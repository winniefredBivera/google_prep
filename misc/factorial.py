"""
FACTORIAL
winniefred bivera
"""

def factorial(no):
    if no in [0, 1]:
        return 1
    else:
        return factorial(no-1)*no
