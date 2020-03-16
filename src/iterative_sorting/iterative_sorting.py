# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(len(arr)-1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]           
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    print(f'original:{arr}')
    print(f'swapping {arr[i]} with {arr[j]}\ncurrent arr: {arr}')

    return arr