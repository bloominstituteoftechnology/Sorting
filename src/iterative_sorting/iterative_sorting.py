test_array = [7, 2, 45, 1, 90, 54, 23, 12, 9, 14]

def insertion_sort(arr):
    # loop through elements
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i
        
        while j > 0 and temp < arr[j - 1]:
            # shift left until correct position is found
            arr[j] = arr[j-1]
            j -= 1

        arr[j] = temp

    return arr

# print("insertion_sort:", end=" ")
# print(insertion_sort(test_array))

# TO-DO: Complete the selection_sort() function below 
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

# print("selection_sort: ", end='')
# print(selection_sort(test_array))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swaps = 1

    while swaps > 0:
        swaps = 0
        for i in range(0, len(arr)-1):
            # Swap if wrong positions
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                swaps += 1
    return arr

# print("bubble_sort: ", end='')
# print(bubble_sort(test_array))

test_array = [9,3,1,5,7,2,5,8,2,5,9,5,1,4,7,9,4,2,3,6]
# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=10 ):
    # Array is 0 - 9. Initialize empty values
    count = [0 for i in range(0, maximum)]

    # count the numbers we have in the array:
    for i in range(0, len(arr)):
        if arr[i] < 0:
            return "Error, negative numbers not allowed in Count Sort"
        count[arr[i]] += 1

    new_arr = [0 for i in range(0, len(arr))]
    j = 0
    for i in range(0, maximum):
        while count[i] > 0:
            new_arr[j] = i
            count[i] -= 1
            j += 1

    return new_arr

# print(count_sort(test_array))