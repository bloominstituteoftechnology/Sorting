# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        for index in range(i, len(arr)):
            if arr[smallest_index]>arr[index]:
                # print("This one: ", arr[smallest_index], 'this other one', arr[index])
                smallest_index = index
        smaller = arr[smallest_index]
        cur = arr[i]
        arr[i] = smaller
        arr[smallest_index] = cur
        # print(smaller, cur)
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
             



        # TO-DO: swap




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    unsorted = True
    bubble_range = range(1, len(arr))
    while True:
        stop = True
        # print(range(len(arr)-1), bubble_range)
        for i, x in zip(range(len(arr)), bubble_range):
            if arr[i]>arr[x]:
                min = arr[x]
                max = arr[i]
                arr[i] = min
                arr[x] = max
                stop = False
        if stop == True:
            break

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr