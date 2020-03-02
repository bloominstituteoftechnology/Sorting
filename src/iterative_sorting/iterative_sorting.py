
arr = [1, 3, 4, 68, 3, 244, 40, 112, 342, 543,
       45, 21, 2, 4, 5, 7, 8, 4, 3, 45, 78, 9]


# TO-DO: Complete the selection_sort() function below


def selection_sort(arr):
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
        numb = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = numb

        # TO-DO: swap

    return arr


print(selection_sort(arr))

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    swap = True
    while swap:
        # for i in range(0, len(arr)):
        swap = False
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp_var = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp_var
                swap = True

    # swap = True
    # while swap:
    #     # swap = False
    #     for i in range(0, len(arr)):
    #         if arr[i] > arr[i + 1]:
    #             arr[i] = arr[i + 1]
    #             swap = True

    return arr


print(bubble_sort(arr))

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):
    # count = arr_of_numb[]
    # count = 0
    # for numb in arr:
    #     count[numb - min] = count[numb - min] + 1

    # arb_numb = 0
    # for i
    return arr
