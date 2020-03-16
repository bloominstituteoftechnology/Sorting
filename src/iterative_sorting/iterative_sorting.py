# TO-DO: Complete the selection_sort() function below

"""Start with current index = 0
For all indices EXCEPT the last index:
a. Loop through elements on right-hand-side of current index
    find the smallest element
b. Swap the element at current index with the smallest element found in above loop
"""

#original question
# def selection_sort(arr):
#     # loop through n-1 elements
#     for i in range(0, len(arr) - 1):
#         cur_index = i
#         smallest_index = cur_index
#         # TO-DO: find next smallest element
#         # (hint, can do in 3 loc)
#
#         # TO-DO: swap
#
#     return arr

def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
# TO-DO: find next smallest element
# (hint, can do in 3 loc)
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                place_holder = arr[smallest_index]
                # arr[i], arr[place_holder] = arr[place_holder], arr[i]
                ##close! doesnt handle last index or move 3rd to last?
# TO-DO: swap
                arr[smallest_index] = arr[j]
                arr[j] = place_holder

    return arr


# TO-DO:  implement the Bubble Sort function below
'''Loop through your array
Compare each element to its neighbor
If elements in wrong position (relative to each other, swap them)
If no swaps performed, stop. Else, go back to the element at index 0
repeat step 1.
'''


def bubble_sort(arr):
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    return arr
