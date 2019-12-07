# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # Find minimum element
        cur_index = i
        # print("I am i in 1st loop:", cur_index)
        # have to not do len(arr) - 1 to access last element
        for j in range(i+1, len(arr)):
            # print("I am J: ", j)
            # print("J Loop 1. I am arr[cur_index]", arr[cur_index])
            # print("J Loop 2. I am arr[j]", arr[j])
            if arr[cur_index] > arr[j]:
                cur_index = j  # Looping through values in array and setting cur_index to the array number that is the smallest
                # print("J Loop >. cur_index set to j", cur_index)

        # Swap minimum element
        # print("I occur after j loop finishes then goes back to i loop -> j loop")
        # Current number you are on in the i for loop. Setting x to be first array number
        x = arr[i]
        # print("1. I am x", x)
        # print("2. I am arr[cur_index]", arr[cur_index])
        # arr[cur_index] is the lowest number found and being set to current i position(being near beginning. So smallest going to front of array)
        # position arr[i] is being set to the lowest number found in j loop. Swap begins
        arr[i] = arr[cur_index]
        # print("3. I am arr[i] being set to to arr[cur_index]", arr[i])

        arr[cur_index] = x  # index that had the smallest number being swapped
        # The index where the smaller number was is now getting the bigger number
        # print("4. ", arr[cur_index])

    return arr


selection_sort([5, 3, 4, 2, 1])


# TO-DO:  implement the Bubble Sort function below
# bubble sort works by repeatedly swapping adjacent elements if they are in the wrong order
def bubble_sort(arr):
    # set x equal to length of arrya
    x = len(arr)

    for i in range(x):
        # print("I am I: ", i)
        for j in range(0, x-i-1):  # range of 0, len(arr) - i - 1. Initially will be len(arr) - 0 - 1
            # print("I am j: ", j)
            if arr[j] > arr[j+1]:
                # Line below is same as arr[j] = arr[j+1] and arr[j+1] = arr[j]
                # Swapping the small and big numbers.
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


bubble_sort([5, 3, 4, 2, 1])
# Ex after first I loop (0):
# [3,4,2,1,5]
# I loop(1):
# [3,2,1,4,5]
# I loop(2):
# [2,1,3,4,5]
# I loop(3):
# [1,2,3,4,5]


# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
