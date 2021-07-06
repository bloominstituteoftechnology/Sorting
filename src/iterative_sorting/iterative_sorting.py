# TO-DO: Complete the selection_sort() function below 

number_array = [10, 5, 147, 18, 7, 348, 49, 33, 8, 29, 4, 3, 16, 90, 86, 91, 70, 9, 11, 28]


def selection_sort(arr):
    # loop through n-1 elements
    for n in range(0, len(arr) - 1):

        cur_index = n
        smallest_index = cur_index

        for x in range(n+1, len(arr)):
            if arr[smallest_index] > arr[x]:
                smallest_index = x
        would_be_first = arr[cur_index]
        would_be_second = arr[smallest_index]

        arr[cur_index] = would_be_second
        arr[smallest_index] = would_be_first

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        # TO-DO: swap

    return arr

# print(selection_sort(number_array))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    index = 0
    count = 0
    loop = True

    while loop:
        count = 0
        for n in range(0, len(arr)-1):
            if arr[n] > arr[n+1]:
                value = arr[n]
                arr[n] = arr[n+1]
                arr[n+1] = value
                count += 1
        if count == 0:
            loop = False
            break

    return arr

print(number_array)
print(bubble_sort(number_array))


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr