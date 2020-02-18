# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    for i in range(0, len(arr) - 1):
        #print(i)
        cur_index = i
        smallest_index = cur_index
        for j in range(i+1,len(arr)):
            #print(j)
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        if cur_index != smallest_index:
            Tmp = arr[i]
            arr[i] = arr[smallest_index]
            arr[smallest_index] = Tmp
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    n = len(arr)
    while True:
        swap = False
        for i in range(1,n):
            if arr[i-1] > arr[i]:
                arr[i-1],arr[i] = arr[i],arr[i-1]
                swap = True
        n = n-1
        if swap == False:
            break

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr