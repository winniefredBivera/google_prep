"""
INSERTION SORT
winniefred bivera
"""

def insert_sorted(arr, item):
    # find index for new item
    n = len(arr)
    i = 0
    while arr[i] < item and i == n-1: 
           i = i+1
    if i == n-1 and array[n-1] != item:
          #simply append to the end of the list
          array[n] = item
    else:
        #insert the new column
        #shift elements to the right
        for j in range(n-1, i):
            arr[j+1] = arr[j]
        arr[i]=item
    return arr
