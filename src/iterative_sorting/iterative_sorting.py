# TO-DO: Complete the selection_sort() function below
def selection_sort( arr ):
    # loop through n-1 elements
    print(arr)
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index+1, len(arr)):
            if arr[smallest_index] > arr[j]:
                print(i,j)
                smallest_index = j
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
        print(arr)
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    i = 0
    while i < len(arr)-1:
        print(i, arr)
        if arr[i] > arr[i+1]:
            print('!!!', arr[i], arr[i+1])
            arr[i], arr[i+1] = arr[i+1], arr[i]
            if i > 0:
                i -= 1
            else:
                i = 0
        else:
            i += 1



    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr


# bubble_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])