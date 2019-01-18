# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        current_index = i
        smallest_index = current_index
        # print(arr[i])
        # print(arr)

        # Find Smallest
        for comparison_index in range(current_index, len(arr)):
            # print(arr[comparison_index])
            if arr[comparison_index] < arr[smallest_index]:
                smallest_index = comparison_index
            
        # Swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[current_index]
        arr[current_index] = temp
    
    return arr

# print(selection_sort([5,34,2,5,7,3,9,10]))

# TO-DO: implement the Insertion Sort function below

# Iterative
# def insertion_sort( arr ):
#     current_index = 1 # Start with the second item in the array
#     while current_index < len(arr): # Go through each position in the array 
#         cur_item = arr[current_index] # Get the current item to compare
#         comparison_index = current_index - 1 # Get the index of the item left of the current item
#         # print('loop:' + str(current_index))
#         # print(cur_item)

#         # Shift
#         while comparison_index >= 0 and arr[comparison_index] > cur_item: # Shift items until the beginning of the array is reached, or a smaller item is found.
#             # print(arr)
#             arr[comparison_index+1] = arr[comparison_index] # Shift the item currently being compared to with the item right of it.
#             comparison_index -= 1 # Next Loop, compare to the item left of the item currently being compared.

#         # Insert
#         arr[comparison_index+1] = cur_item # Insert the item into the original position of the last item that was shifted.
#         current_index += 1 # Next Loop, check the item right of the original position of the item that was just checked.

#     return arr

def insertion_sort(unsorted, sorted = [], n = 1, state = 'shift'):
    if state == 'shift':
        if len(unsorted) > 0:
            sorted = insertion_sort([], sorted, unsorted[0], 'insert')
            return insertion_sort(unsorted[1:], sorted)
        else:
            return sorted
    else:
        if sorted == []:
            return unsorted + [n]
        if n < sorted[0]:
            return unsorted + [n] + sorted
        return insertion_sort(unsorted + sorted[:1], sorted[1:], n, 'insert')

# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):
    sorted = False
    while sorted == False:
        sorted = True
        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]:
                temp = arr[i]
                arr[i] = arr[i - 1]
                arr[i - 1] = temp 
                sorted = False
    return arr

# print(bubble_sort([5,34,2,5,7,3,9,10]))


# STRETCH: implement the Count Sort function below
def count_sort(arr):
    
    if arr == []:
        return []

    maximum = max(arr)
    count = []
    final = list(arr)

    for i in range(0, maximum + 1):
        count.append(0)
    
    for i in arr:
        if i >= 0:
            count[i] += 1
        else:
            return 'Error, negative numbers not allowed in Count Sort'

    for i in range(1, maximum + 1):
        count[i] += count[i-1]
    
    for i in reversed(final):
        arr[count[i] - 1] = i
        count[i] -= 1

    return arr

# print(count_sort([5,34,2,5,7,3,9,10]))