# Complete the selection_sort() function below in class with your instructor
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        temp = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temp

    return arr


# TO-DO: implement the Insertion Sort function below
arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key

    return arr

# STRETCH: implement the Bubble Sort function below


def bubble_sort(arr):
    n = len(arr)
    # loop through the array
    for i in range(n):

        for j in range(0, n-i-1):
            # swap if the element found is greater
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

# STRETCH: implement the Count Sort function below


def count_sort(arr):
    if len(arr) > 0:
        m = max(arr)
    if len(arr) > 0 and min(arr) > 0:
        m = max(arr)
    elif len(arr) == 0:
        return []
    else:
        if min(arr) < 0:
            return 'Error, negative numbers not allowed in Count Sort'

    # creates an array of zeros that matches the length of the passed in array
    n = [0 for i in range(m + 1)]
    sorted_arr = []
    for i in arr:
        print(i)
        n[i] += 1
    for i in range(len(n)):
        if n[i] != 0:
            sorted_arr += [i for n in range(n[i])]

    return sorted_arr


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
arr2 = []
arr3 = [1, 5, -2, 4, 3]
print(count_sort(arr3))
