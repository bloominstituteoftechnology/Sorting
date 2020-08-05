# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range (cur_index+1,len(arr)):
            #compare all values to value of curr index
            # find the smallest 
            if arr[j]<arr[smallest_index]:
                smallest_index=j
        # TO-DO: swap
        arr[cur_index],arr[smallest_index]=arr[smallest_index],arr[cur_index]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    made_a_swap= True
    while made_a_swap:
        made_a_swap = False

        for i in range(0,len(arr)-1):
            j = i+1

            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
                made_a_swap=True
    
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr