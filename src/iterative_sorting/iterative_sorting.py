# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        # find smallest element
        for j in range(cur_index, len(arr)):
            if(arr[smallest_index] > arr[j]):
                smallest_index = j
        if(arr[cur_index] > arr[smallest_index]):
            low = arr[smallest_index]
            high = arr[cur_index]
            #now do the swith or moving around in given array
            arr[cur_index] = low
            arr[smallest_index] = high        
        
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    n = len(arr)

    # go through element of the array
    for i in range(n):
        #last element of the array 
        for j in range(0, n-i-1):
            # going through bubble sort go through elements again and keep
            # switching until elements allign
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    #start counter
    counter = [0]*(maximum + 1)
    # then enumerate
    for i in arr:
        counter[i] += 1
        del arr
        arr = []
    for number, amount in enumerate(counter):
        arr += [number] * amount
    return arr

# debug the count sort in print statement:
my_list = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

my_new_list = count_sort(my_list, 9)
print (my_list)

print (my_new_list)
