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

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

def insertion_sort(arr):
    for i in range(1, len(arr)):

        # while position is at least 1 and
        while i > 0 and arr[i - 1] > arr[i]:
            arr[i] = arr[i -1]

    print(arr)



# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

insertion_sort(arr1)