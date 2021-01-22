"""
BINARY SEARCH
winniefred bivera
"""


def binary_search_recursive(arr, key, n_low, n_high):
    n_middle = int((n_low + n_high)/2)
    if n_low == n_high:
        return None
    if arr[n_middle] == key:
        return n_middle
    elif arr[n_middle] > key:
        output = binary_search_recursive(arr, key, n_low, n_middle - 1)
    else:
        output = binary_search_recursive(arr, key, n_middle + 1, n_high)
    return output


def binary_search_iterative(arr, key):
    n_high = n = len(arr)
    n_middle = n_low = 0

    while True:
        n_middle = int((n_low + n_high)/2)
        if arr[n_middle] == key:
            return n_middle
        elif n_low > n_high:
            return None
        else:
            if arr[n_middle] > key:
                n_high = n_middle - 1
            else:
                n_low = n_middle + 1
