# TO-DO: Complete the selection_sort() function below
arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # print(smallest_index)
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # swap_index = arr.index(min(arr[i:]))
        # for k in range(i, len(arr)):
        #     if (arr[k] < arr[smallest_index]):
        #         smallest_index = k
        for k in range(0, len(arr[i:])):
            if (arr[k+i] < arr[smallest_index]):
                smallest_index = k+i
        # print(swap_index)
        # TO-DO: swap
        # arr[smallest_index], arr[swap_index] = arr[swap_index], arr[smallest_index]
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr


print(selection_sort(arr))


# TO-DO:  implement the Bubble Sort function below
arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]


def bubble_sort(arr):
    # check if need to continue to loop
    counter = len(arr)-1
    while counter > 0:
        counter = len(arr)-1
        # loop through elements
        for i in range(0, len(arr) - 1):
            # print(f"index: {i}, list: {arr}, counter: {counter}")
            # compare element against neighbor:
            if(arr[i] > arr[i+1]):
                # if larger, swap positions
                arr[i], arr[i+1] = arr[i+1], arr[i]
            # decrease counter by 1 every time there is no swap
            else:
                counter -= 1
    return arr


print(bubble_sort(arr))

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
