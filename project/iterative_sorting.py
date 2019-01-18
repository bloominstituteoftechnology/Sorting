# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j   



        # TO-DO: swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp



    return arr


# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):
    for index in range(1, len(arr)):
        cur_value = arr[index]
        position = index

        while position > 0 and arr[position - 1] > cur_value:
            arr[position] = arr[position - 1]
            position = position - 1

        arr[position] = cur_value

    return arr


# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):
    for passnum in range(len(arr) - 1, 0, -1):
        for i in range(passnum):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    if len(arr) == 0:
        return arr
    
    if maximum == -1:
        maximum = max(arr)
    count = [0] * (maximum + 1)               
    for a in arr:
        if a < 0:
            return "Error, negative numbers not allowed in Count Sort"
        else:
            count[a] += 1             

    j = 0
    for i in range(0, len(count)):            
        while count[i] > 0:
            arr[j] = i
            j += 1
            count[i] -= 1

    return arr