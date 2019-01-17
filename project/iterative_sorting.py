# Complete the selection_sort() function below in class with your instructor
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # swap
        temp = arr[smallest_index]
        # take the item at the current i, move it to where smallest item was
        arr[smallest_index] = arr[cur_index]
        # take smallest item put at current index
        arr[cur_index] = temp

    return arr


# implement the Insertion Sort function below
def insertion_sort(arr):
    # After first index
    for i in range(1, len(arr)):
        temp = arr[i]
        # iterate to left
        for j in range(len(arr[:i]), -1, -1):
            if temp < arr[j]:
                # slide item over ->
                arr[j+1] = arr[j]
                # insert temp at index
                arr[j] = temp

    return arr


# STRETCH: implement the Bubble Sort function below
def bubble_sort(arr):
    swapped = True
    # loop
    while swapped:
        swapped = False
        for i in range(1, len(arr)):
            temp = arr[i]
            if arr[i - 1] > arr[i]:
                # swap
                arr[i] = arr[i-1]
                arr[i-1] = temp
                swapped = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    maximum = 10
    # find max
    for i in arr:
        if i > maximum:
            maximum = i
    # create an array of k zeros
    count = [0] * maximum
    output = [0] * len(arr)
    # count number of each arr[i]
    for i in arr:
        count[i] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    for i in range(len(arr)):
        output[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1

    return output


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
arr2 = [1, 4, 1, 2, 7, 5, 2]
print(count_sort(arr2))
