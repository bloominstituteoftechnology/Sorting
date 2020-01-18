# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr)-1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for select in range(cur_index, len(arr)):
            if arr[select] < arr[smallest_index]:
                smallest_index = select

        if cur_index != smallest_index:
            smallest_item = arr.pop(smallest_index)
            cur_item = arr.pop(cur_index)
            arr.insert(cur_index, smallest_item)
            arr.insert(smallest_index, cur_item)
        




    return arr




# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    sorted = False
    while not sorted:
        swaps = 0
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i+1]:
                swaps += 1
                item = arr.pop(i)
                arr.insert(i+1, item)
        if swaps == 0:
            sorted = True
    return arr

print(selection_sort([1, 5, 8, 4, 0, 3, 7, 2, 9, 6]))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr