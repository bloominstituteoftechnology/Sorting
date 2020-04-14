# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
             



        # TO-DO: swap




    return arr

input_array = [2, 54, 11, 1, 145, 8]

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0, len(arr)):
        for index in range(1, len(arr)):
            current = arr[index]
            previous = arr[index - 1]
        
            if previous <= current:
                continue
            else:
                arr[index] = previous
                arr[index - 1] = current
    
    return arr

print(bubble_sort(input_array))


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr