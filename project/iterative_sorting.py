# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

 # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 

        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

 # TO-DO: swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr



# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):
    
    for i in range(0, len(arr)):
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j] 
            j -= 1
        
        arr[j+1] = key 

    return arr


# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr