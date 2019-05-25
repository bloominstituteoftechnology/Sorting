# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i+1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
           
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
        # TO-DO: swap
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i+1]:
                swapped = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]    

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    output = [0 for i in range(maximum)]
    count = [0 for i in range(maximum)]
    ans = ["" for _ in arr]
    for i in arr:
        count[ord(i)] += 1
    for i in range(len(arr)):
        output[count[ord(arr[i])]-1] = arr[i]
        count[ord(arr[i])] -= 1
    
    for i in range(len(arr)):
        ans[i] = output[i]
    
    return ans