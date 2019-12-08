# Complete the selection_sort() function below
def selection_sort( arr ):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i
        while j > 0 and temp < arr[j-1]:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = temp
    return arr
             

# Implement the Bubble Sort function below
def bubble_sort( arr ):
    while True:
        swap = 0
        for i, val in enumerate(arr):
            if i == len(arr)-1: 
                break
            left = arr[i]
            right = arr[i+1]
            if left > right:
                arr[i] = right
                arr[i+1] = left
                swap += 1
        if swap > 0:
            continue
        else: break
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
