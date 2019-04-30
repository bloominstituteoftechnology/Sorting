# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print(arr)
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0 , len(arr)-1):
        print('~~~~~~~~~~~~~~')
        print(len(arr) -1)
        for j in range(0, len(arr)-1-i):
            print(len(arr)-1-i)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)
    return arr

bubble_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr