# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        min_el = arr[i]
        for a in range(i, len(arr)):
            if arr[a] < min_el:
                min_el = arr[a]

        # TO-DO: swap
        arr.remove(min_el)
        arr.insert(i, min_el)
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ): #O(n^2)          #e.g arr = [1, 2, 3, 4, 5, 6]
    # arrLength = len(arr)                 #6

    # for a in range(arrLength):           # a = 1, 2, 3, 4, 5, 6 in newline
    #     for b in range(0, arrLength-a-1): # check 1 from (0 to 4)
    #         if(arr[b] > arr[b+1]):        # if 1 > next index of 2 which is 2
    #             arr[b], arr[b+1] = arr[b+1], arr[b]  #switch i.e 2, 1 which is false
    #         else:
    #             arr[b+1], arr[b] = arr[b+1], arr[b]  #switch i.e 1, 2 which is true
    # return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])