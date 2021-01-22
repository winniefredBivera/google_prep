"""
FIBONACCI MEMORIZATION
implementation of fibonacci number generation using memorization for improved performance
winniefred bivera
"""

memory = {}

def memorize_and_remember(function):
    def wrapper_over_fibonacci(n):
        if n in memory.keys():
            output = memory[n]
        else:
            output = function(n)
            memory[n] = output
        return output
    return wrapper_over_fibonacci

@memorize_and_remember
def fibonacci(n):
    if n in [0,1]:
        output = 1
    else:
        output = fibonacci(n-1) + fibonacci(n-2)
    return output
