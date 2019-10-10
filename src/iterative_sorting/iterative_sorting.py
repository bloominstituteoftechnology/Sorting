# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(len(arr)):
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swapped = True 
    while swapped: # while swapped is True, runnit
        for i in range(len(arr)):
            swapped = False # swapped is now Faaaaalse
            for j in range(i + 1, len(arr)): # two loops but j is +1
                if arr[i] > arr[j]: # if i > j
                    arr[i], arr[j] = arr[j], arr[i] # switcheroo
                    swapped = True # swappy is now true
        return arr


# STRETCH: implement the Count Sort function below

def counting_sort(array, maxval):
    """in-place counting sort"""
    m = maxval + 1
    count = [0] * m # init with zeros
    for a in array:
        count[a] += 1 # count occurences
    i = 0
    for a in range(m): # emit
        for c in range(count[a]): # - emit 'count[a]' copies of 'a'
            array[i] = a
            i += 1
    return (array,count)