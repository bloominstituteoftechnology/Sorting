# TO-DO: Complete the selection_sort() function below
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)




        # TO-DO: swap




    return arr

array = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

# array = [1, 5, 4, 2, 8]
#
# array = [1, 4, 5, 2, 8]
#
# array = [1, 4, 2, 5, 8]


# array = [1, 4, 2, 5, 8]
#
# array = [1, 4, 2, 5, 8]
#
# array = [1, 2, 4, 5, 8]
#
# array = [1, 2, 4, 5, 8]


# [1, 4, 2, 5, 8] 1'st pass

# TO-DO:  implement the Bubble Sort function below



def bubble_sort( arr ):
    swap_occured = True

    while swap_occured:
        swap_occured = False
        for index in range(0, len(arr) - 1):
            # index is left hand value
            #j is right hand value
            j = index + 1

            temp = arr[j]

            if arr[index] > arr[j]:
                arr[j] = arr[index]
                arr[index] = temp
                swap_occured = True

    return arr

print(bubble_sort(array))
# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
