# Complete the selection_sort() function below
def selection_sort( arr ):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i
        while j > 0 and temp < arr[j-1]:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = temp
    return arr
             

# Implement the Bubble Sort function below
def bubble_sort( arr ):
    while True:
        swap = 0
        for i, val in enumerate(arr):
            if i == len(arr)-1: 
                break
            left = arr[i]
            right = arr[i+1]
            if left > right:
                arr[i] = right
                arr[i+1] = left
                swap += 1
        if swap > 0:
            continue
        else: break
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr):
    if len(arr) == 0: return arr
    min_value = max_value = arr[0]

    #find min and max variables
    for v in range(len(arr)):
        if arr[v] < 0: return 'Error, negative numbers not allowed in Count Sort'
        elif arr[v] < min_value: min_value = arr[v]
        elif arr[v] > max_value: max_value = arr[v]
    
    #create empty list of n size
    count_array = [0] * (max_value-min_value+1)

    #do the counting
    for n in range(len(arr)):
        count_array[arr[n]-min_value] += 1

    #sort array
    arr = []
    for i in range(len(count_array)):
        for n in range(count_array[i]):
            arr.append(i+min_value)

    return arr
