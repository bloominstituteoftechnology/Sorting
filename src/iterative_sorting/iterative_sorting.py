
# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index #by default currect is smallest
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for m in range(cur_index, len(arr)):
            if arr[m] < arr[smallest_index]:
               smallest_index = m  
              # TO-DO: swap 
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
        
    return arr
print(selection_sort([2,4,2,9,5,1]))       

        # temp = arr[cur_index]  # hold the smallest index from loop. then swap
        # arr[cur_index] = arr[smallest_index] #add smallest index with current index
        # arr[cur_index] = temp # current index now will equal new smallest index

  


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swapped = True #run as long as swapped is true
    while swapped:
        swapped = False
        for i in range(0, len(arr) -1): # -1 exclude last index
            if arr[i] > arr[i+1]: # if the current element is greater than interate to right
                arr[i], arr[i+1] = arr[i+1], arr[i] #swap
                swapped = True #break

    return arr

# print(selection_sort(arr))


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
