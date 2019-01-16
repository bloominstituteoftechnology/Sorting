# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # find next smallest element
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr


# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):

    for i in range(1, len(arr)):
        # print(arr[i])
        index = i 
        while index > 0 and arr[index - 1] > arr[index]:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index = index - 1

    return arr

print(insertion_sort([1,5,6,2,3]))


# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):

    for i in range(0, len(arr) - 1):
        swapped = False

        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if swapped == False:
            break

    return arr

print(bubble_sort([1,5,6,2,3]))


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    # create a new array the size of largest - smallest filled with 0's
    index = [0 for i in range(0, max(arr) + 1)]

    # loop over existing arr and the index 
    # of the ammount in the new_arr += 1
    for i in range(0, len(arr) - 1):
        index[arr[i]] += 1

    
    return arr

print(count_sort([1,5,1,6,2,5,3]))