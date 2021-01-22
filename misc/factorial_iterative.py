"""
FACTORIAL ITERATIVE
winniefred bivera
"""

def factorial(n):
    arr = []
    for i in range(n+1):
        if i in [0,1]:
            output = 1
        else:
            output = i*arr[i-1]
        arr.append(output)
    return arr[n]
