# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for n in range(smallest_index+1, len(arr) ):
            # If the value at n is smaller than the value
            # at smallest_index, swap them
            if arr[n] < arr[smallest_index]:
                pivot = arr[smallest_index]
                arr[smallest_index] = arr[n]
                arr[n] = pivot
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    count = 0
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        second_index = i + 1
        # if the number right in smaller that the smallest_index:
        if arr[second_index] < arr[smallest_index]:
            pivot = arr[smallest_index]
            arr[smallest_index] = arr[second_index]
            arr[second_index] = pivot
            count += 1
    #check that it has been not changes or swaps
    if count > 0:
        selection_sort(arr)
    return arr


# STRETCH: implement the Count Sort function below
# Video: https://www.youtube.com/redirect?v=7zuGmKfUt7s&event=video_description&q=http%3A%2F%2Fwww.geeksforgeeks.org%2Fcounting-sort%2F&redir_token=IEcQm-hylFwxrPj5izBbWl1NHTB8MTU4MjE0MzQwOEAxNTgyMDU3MDA4
def count_sort( arr, maximum=-1 ):
    # counting number of eleements having distinct keys
    # doing dome arithmetic to calculate the positions 
    # of each element in the output ()
    max = arr[0]
    # check what is the maximun value in the array
    for x in arr:
        if x > max:
            max = x
    # create a counter with the same size than
    # the maximun number of the input 
    counter = [0] * (max+1)
    # counter = [0 for i in range(max+1)]
    # create the output array that it's going to
    # content the sln
    output = [0] * len(arr)
    # output = [0 for _ in arr]
    indexes = range (1,max+1)
    # count each element in arr and place the count
    # at the appropiate index in the counter array
    for n in arr: 
        counter[n]+= 1
    # modify the counter array by adding
    # the previous counts
    for i in indexes:
        counter[i] +=counter[i-1]
    # for each element in the initial array find this 
    # index in counter and substract 1. The value
    # in counter is used as index in the output array 
    # and we save there the value from the inital array
    for x in arr:
        output[counter[x]-1]=x
        counter[x]-=1
    return output
    