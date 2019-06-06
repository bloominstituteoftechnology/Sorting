# TO-DO: Complete the selection_sort() function below 

#[7, 3, 12, 6, 20, 4, 2

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # i position in for loop is used to place next smallest number
        smallest_index = i
        for j in range(i + 1, len(arr)):
            #j searches through positions of i + 1 to end of list
            if arr[smallest_index] > arr[j]:
                #if current index(i, aka smallest index)

                smallest_index = j
                
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]


    print(arr)
    return arr
selection_sort([7, 3, 12, 6, 20, 4, 2])

# TO-DO:  implement the Bubble Sort function below

#[1, 3, 12, 6, 20, 4, 2]

def bubble_sort( arr ):
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) -1 -i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # print(arr)
    return arr
    

bubble_sort([1, 3, 12, 6, 20, 4, 2])


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr