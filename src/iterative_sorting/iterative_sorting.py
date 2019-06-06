# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        temp =  arr[i]
        while smallest_index > 0 and temp < arr[smallest_index - 1]:
            arr[smallest_index] = arr[smallest_index - 1]
            smallest_index -= 1
        arr[smallest_index] = temp
        # TO-DO: swap

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swapped = True

    while swapped:
      swapped = False
      for num in range(0, len(arr) - 1):
        if arr[num] > arr[num + 1]:
          arr[num] , arr[num + 1] = arr[num + 1], arr[num]
          swapped = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr