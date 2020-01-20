arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]


# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for checkIndex in range(cur_index, len(arr)):
            if arr[checkIndex] < arr[smallest_index]:
                smallest_index = checkIndex
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
        cur_index += 1
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        # TO-DO: swap

    return arr


print(selection_sort(arr1))

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for index in range(len(arr)):
            if index == 0:
                continue
            if arr[index] < arr[index - 1]:
                arr[index], arr[index - 1] = arr[index - 1], arr[index]
                swapped = True
    return arr


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
bubble_sort(arr1)
print(arr1)

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    # keep track of what the largest value is in the array
    # iterate over array, upping max if needed
    count = dict()
    for item in arr:
        if item < 0:
            return "Error, negative numbers not allowed in Count Sort"
        maximum = max(maximum, item)
        count[item] = count.get(item, 0) + 1

    # from 0 through maximum, add the count for the previous value to each count, cumulatively
    for i in range(maximum+1):
        if i == 0:
            count[i] = count.get(i, 0)
        count[i] = count.get(i, 0) + count.get(i - 1, 0)
    # create an empty array *maximum* long
    out = [None for y in range(len(arr))]
    # iterate over original input array - look up the value in the dict using the original value as key and insert that value in the new, empty array at the 'count' index.
    for toSort in arr:
        newIndex = count[toSort] - 1
        out[newIndex] = toSort
        # decrement the dict 'count' value
        count[toSort] -= 1

    return out


arr2 = [1, 4, 1, 2, 7, 5, 2]
arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
arr1 = count_sort(arr1)
arr2 = count_sort(arr2)
print(arr1)
print(arr2)
