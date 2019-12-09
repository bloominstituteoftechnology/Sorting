# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        index = i
        smallest_index = index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        temp = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temp
        # TO-DO: swap

    return arr
print(selection_sort([5,2,1,9,0,4,6]))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    arrLength = len(arr) -1
    for i in range(arrLength):
        for j in range(arrLength - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j +1], arr[j]
    return arr
print(bubble_sort([5,2,1,9,0,4,6]))



# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr