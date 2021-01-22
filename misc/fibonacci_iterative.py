"""
ITERATIVE FIBONACCI
"""

def fibonacci(n):
    arr = []
    for i in range(n+1):
        if i in [0,1]:
            arr.append(1)
        else:
            output = arr[i-1] + arr[i-2]
            arr.append(output)
    return arr[n]
