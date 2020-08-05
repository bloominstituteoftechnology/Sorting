# TO-DO: Complete the selection_sort() function below 

arr = [5, 3, 10, 2, 1]
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = cur_index
                smallest_index = j
                print(j)        
             
        # TO-DO: swap
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr

"""print(selection_sort( arr ))"""

# TO-DO:  implement the Bubble Sort function below
lizzy = [5, 3, 10, 2, 1, 0, 12, 89, 2, 90]
def bubble_sort( arr ):
    swapped = True
    while swapped:
        swapped = False
        for j in range(len(arr) -1):
            check = j + 1
            if arr[j] > arr[check]:
                swapped = True
                arr[j], arr[check] = arr[check], arr[j]

        print("ARRR", arr)
    
    

    return arr
print(bubble_sort(lizzy))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr