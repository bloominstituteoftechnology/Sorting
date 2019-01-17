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
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr

# TO-DO: implement the Insertion Sort function below


def insertion_sort(arr):
    # i = 1

    # while i < len(arr):
    #     j = i

    #     while j > 0 and arr[j-1] > arr[j]:
    #         arr[j], arr[j-1] = arr[j-1], arr[j]
    #         j -= 1
    #     i += 1
    # return arr
    if len(arr) == 0:
        return arr

    sortedList = [arr[0]]
    unsorted = arr[1:]

    while len(unsorted) > 0:
        for num in sortedList[::-1]:
            if len(unsorted) == 0:
                return sortedList
            if num < unsorted[0]:

                sortedList.insert(sortedList.index(num) + 1, unsorted[0])
                unsorted.pop(0)
                break
            elif sortedList.index(num) == 0:
                sortedList.insert(0, unsorted[0])
                unsorted.pop(0)

    return sortedList


print(insertion_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))
# STRETCH: implement the Bubble Sort function below


def bubble_sort(arr):
    i = 0
    while i < len(arr)-1:
        for j in range(len(arr) - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j + 1], arr[j]
                i = 0
        i += 1

    return arr

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
