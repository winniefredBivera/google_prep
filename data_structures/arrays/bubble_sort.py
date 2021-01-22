"""
BUBBLE SORT
winniefred bivera
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(0,n-1):
        for j in range(0, n-1):
            if arr[j] > arr[j+1]:
                #swap(a[j], a[j+1])
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1]=temp
    return arr 
