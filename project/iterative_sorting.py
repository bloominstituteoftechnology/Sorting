# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j    
        # TO-DO: swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr


# TO-DO: implement the Insertion Sort function below

# Separate the first element from the rest of the array. Think about it as a sorted list of one element.
# For all other indices, beginning with [1]:
# a. Copy the item at that index into a temp variable
# b. Iterate to the left until you find the correct index in the "sorted" part of the array at which this element should be inserted
# Shift items over to the right as you iterate
# c. When the correct index is found, copy temp into this position

def insertion_sort( arr ):

    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                temp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = temp
            else:
                break

    return arr

# arr = [2,5,9,7,4,1,3,8,6]
# print(arr)
# arr = insertion_sort( arr )
# print(arr)

# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr