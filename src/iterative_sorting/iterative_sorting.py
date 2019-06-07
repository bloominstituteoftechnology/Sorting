# TO-DO: Complete the selection_sort() function below 



def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        #print(arr[smallest_index], smallest_index, cur_index) 
        while cur_index < len(arr) - 1:

            if arr[cur_index + 1] < arr[cur_index]:
                temp = arr[cur_index]
                arr[cur_index] = arr[cur_index + 1]
                arr[cur_index + 1] = temp
                cur_index=0
            else: 
                cur_index += 1
    
            



        # TO-DO: swap




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    i = 0

    while i < len(arr) - 1:

            if arr[i + 1] < arr[i]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                i=0
            else: 
                i += 1
    
            


    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr


test = [3,2,1,6,7,8,9,7]

selection_sort(test)