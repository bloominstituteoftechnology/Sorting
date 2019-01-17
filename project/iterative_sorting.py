# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 

        for j in range(i + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                # Swap the found minimum element with the first element
                # if it is smaller than current smallest_index
                smallest_index = j
                # switches index value not the actual number itself
        #  This swaps initial value (first value) with new smallest value
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr

print(selection_sort([3,2,5,8,2]))
# TO-DO: implement the Insertion Sort function below
def insertion_sort(arr):
    for i in range(1, len(arr)-1):
        key = arr[i]
        shift = i - 1
        while shift >= 0 and key < arr[shift]:
            arr[shift + 1] = arr[shift]
            shift -= 1
        arr[shift + 1] = key
    return arr


print(insertion_sort([3,2,5,8,2]))

# STRETCH: implement the Bubble Sort function below

#                                       NOTES FROM WIKI
# Take an array of numbers " 5 1 4 2 8", and sort the array from lowest number to greatest number using bubble sort.
# In each step, elements written in bold are being compared. Three passes will be required.
#
# First Pass
# ( 5 1 4 2 8 ) → ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1.
# ( 1 5 4 2 8 ) → ( 1 4 5 2 8 ), Swap since 5 > 4
# ( 1 4 5 2 8 ) → ( 1 4 2 5 8 ), Swap since 5 > 2
# ( 1 4 2 5 8 ) → ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), algorithm does not swap them.
# Second Pass
# ( 1 4 2 5 8 ) → ( 1 4 2 5 8 )
# ( 1 4 2 5 8 ) → ( 1 2 4 5 8 ), Swap since 4 > 2
# ( 1 2 4 5 8 ) → ( 1 2 4 5 8 )
# ( 1 2 4 5 8 ) → ( 1 2 4 5 8 )
# Now, the array is already sorted, but the algorithm does not know if it is completed. The algorithm needs one whole pass without any swap to know it is sorted.
#
# Third Pass
# ( 1 2 4 5 8 ) → ( 1 2 4 5 8 )
# ( 1 2 4 5 8 ) → ( 1 2 4 5 8 )
# ( 1 2 4 5 8 ) → ( 1 2 4 5 8 )
# ( 1 2 4 5 8 ) → ( 1 2 4 5 8 )


def bubble_sort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - i - 1): #was out of scope without the -1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            else:
                pass
    return arr


print(bubble_sort([3, 5, 8, 9, 2]))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr