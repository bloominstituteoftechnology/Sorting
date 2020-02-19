# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # create variable to hold the min variable
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i, len(arr)):
            if arr[j] < arr[cur_index]:
                cur_index = j
        temp = arr[i]
        arr[i] = arr[cur_index]
        arr[cur_index] = temp
        # TO-DO: swap
    return arr

print(selection_sort([2, 3, 7, 10, 6, 4, 8]))
select = [2]

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # Get the length of the array
    n = len(arr)
    # traverse the array
    for j in range(len(arr)-1,0,-1):
        for i in range(j):
            if arr[i] > arr[i + 1]:
                swap = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = swap

    return arr
print(bubble_sort([3, 6, 7, 10, 2, 4, 8]))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr