# Complete the selection_sort() function below in class with your instructor
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        # smallest_index = cur_index
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[cur_index]:
                cur_index = j
            if cur_index != i:
                arr[i], arr[cur_index] = arr[cur_index], arr[i]
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

# TO-DO: swap

        return arr


# TO-DO: implement the Insertion Sort function below
def insertion_sort(arr):
    # utilizing swaps
    for i in range(1, len(arr)):
        for j in range(i-1, 0, -1):
            if arr[j] > arr[j+i]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                break
    # utilizing shifts
        # for i in range(1, len(arr)):
        #  currNum = arr[i]
        # for j in range(i-1, 0, -1):
        #     if arr[j] > currNum:
        #         arr[j+1] = arr[j]
        #     else:
        #         arr[j+1] = currNum
        #         break

    # for i in range(1, len(arr)):
    #     j = i -1
    #     while arr[j] > arr[j +1] and j >= 0:
    #         arr[j], arr[j+1] = arr[j+1], arr[j]
    #         j-= 1

    return arr


# STRETCH: implement the Bubble Sort function below
def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j + 1], arr[j]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
