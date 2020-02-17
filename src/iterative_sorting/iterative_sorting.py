# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        # TO-DO: swap

    return arr

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    # Create a loop that starts with the last element of the array and works its way to 0 by subtracting one each step
    for i in range(len(arr)-1, 0, -1):
        # create a loop through the range (ie. if i = 9 loop through 0-8) and assign each value to j
        for j in range(i):
            # compare arr[j] to arr[j+1]. For the first loop this will be arr[0] and arr[1] then arr[1] and arr[2], etc.
            if arr[j] > arr[j+1]:
                # if arr[j] is larger then we will assign a variable the value of arr[j]
                k = arr[j]
                # then we set arr[j] to be equal to arr[j+1]. This is essentailly moving the smaller value to the left by setting it equal to the position we started from
                arr[j] = arr[j+1]
                # finally we "bubble up" the value. We set arr[j+1] to the variable we stored the original value of arr[j] in.
                arr[j+1] = k
    return arr


# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
