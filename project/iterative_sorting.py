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
        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp
    return arr

# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):
    for i in range(0, len(arr)):
        start = arr[i]
        for j in range(i-1, -1, -1):
            if(start < arr[j]):
                temp = arr[j]
                arr[j] = start
                arr[j+1] = temp
    return arr


# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):
    n = len(arr)
    while n > 1:
        new = 0
        for i in range(1, n):
            if arr[i -1] > arr[i]:
                temp = arr[i]
                arr[i] = arr[i-1]
                arr[i-1] = temp
                new = i
            print(arr) 
        n = new + 1
        print('''##################################
/////////////////////////////////////''')
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    rangeList = max(arr) - min(arr)
    sortedList = list(range(0, len(arr)))
    index = [0] * (rangeList + 1)
    for num in arr:
        index[num] += 1
    for i, val in enumerate(index):
        if i != 0:
            index[i] += index[i-1]
    for num in arr:
        index[num] -= 1
        sortedList[index[num]] = num    
    return sortedList