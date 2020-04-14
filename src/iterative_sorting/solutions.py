def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element (hint, can do in 3 loc - lines of code) 
        # First, I need to iterate through the elements that remain in the arr
        for x in range(cur_index, len(arr)):
            # Second, I need to check if the element is smaller than the currently smallest
            if arr[x] < arr[smallest_index]:
                # Third, if this statement is True, I will need to set the new index to be the smallest
                smallest_index = x
        # TO-DO: swap the arr
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


def bubble_sort( arr ):
    sorted_elems = 0
    while sorted_elems != len(arr):
        for i in range(len(arr) - sorted_elems - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        sorted_elems += 1
    return arr


