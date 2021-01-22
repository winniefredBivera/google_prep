"""
REVERSE STRING
winniefred bivera
"""

def reverse_array(arr):
    n = len(arr)
    for i in range(0, int(n/2)):
        temp = arr[i]
        arr[i] = arr[n-1-i]
        arr[n-1-i] = temp
    return arr
