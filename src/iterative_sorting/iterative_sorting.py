# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = 0
        smallest_index = i
        # num = 0
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # print(arr[smallest_index])
        if arr[smallest_index] < arr[cur_index + 1]:
            num = arr[smallest_index]
            print(num)

        # if arr[i] < smallest_index:
        #     print(arr[i])
        # TO-DO: swap

    return arr


c = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
selection_sort(c)

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
