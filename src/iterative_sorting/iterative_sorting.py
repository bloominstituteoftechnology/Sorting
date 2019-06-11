# TO-DO: Complete the selection_sort() function below 


def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
     
        smallest_index = cur_index
        
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for e in range(cur_index, (len(arr))):
       
            if arr[e] < arr[smallest_index]:
                smallest_index = e    
                
        t = arr[smallest_index] #saving 
        print('arr',arr)
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = t

    return arr



# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1 - i): #i already sorted, how does this work
            if arr[j] > arr[j+1]: #checking left and right
                arr[j], arr[j+1] = arr[j+1], arr[j] #switching
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr