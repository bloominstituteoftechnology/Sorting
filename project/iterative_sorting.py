# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for x in range(cur_index + 1, len(arr)):
            if arr[x] < arr[smallest_index]:
                smallest_index = x
        # TO-DO: swap
        if smallest_index != i:
            arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr

print(selection_sort([60, 4, 20, 9, 6]))

# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):
    for i in range(1, len(arr)):
        x = i - 1
        while arr[x] > arr[x + 1] and x >= 0:
            arr[x], arr[x + 1] =  arr[x + 1], arr[x]
            x -= 1
    return arr
    
print(insertion_sort([90, 1, 2, 3, 67]))

# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
