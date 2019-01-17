# Complete the selection_sort() function below in class with your instructor
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO: implement the Insertion Sort function below
def insertion_sort(arr):
    i = 1
    while i < len(arr):
        x = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > x:
            arr[j+1] = arr[j]
            j = j - 1
        # end of nested while
        arr[j+1] = x
        i = i + 1
    # end of parent while loop
    return arr


# STRETCH: implement the Bubble Sort function below
def bubble_sort(arr):
    """
    O(n^2) time complexity
    should be used with smaller lists
    can be used with semi sorted lists.
    arr must be an iterable perferably an array type.
    Will sort in ascending order.
    """
    for element in arr:
        for index in range(len(arr) - 1):
            if arr[index] > arr[index + 1]:
                arr[index], arr[index+1] = arr[index+1], arr[index]

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    """
    algorithm for sorting a collection of objects according to keys that are small integers;
    that is an integer sorting algorithm It operates by counting the number of objects that have
    each distinct key value, and using arithmetic on those counts to determine the positions of each
    value in the output sequence. Time complexity O(n log n)
    """
    if len(arr) == 0:
        return []
    k = max(arr)
    count = [0 for x in range(k+1)]
    output = [0 for x in range(len(arr))]

    for i in range(0, len(arr)):
        if arr[i] < 0:
            return "Error, negative numbers not allowed in Count Sort"
        else:
            count[arr[i]] = count[arr[i]] + 1

    # end of for loop
    for i in range(2, len(arr)):
        count[i] = count[i] + count[i-1]
    # end of for loop
    i = len(arr) - 1

    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i]]] = arr[i]

  # end of for loop


    return output
