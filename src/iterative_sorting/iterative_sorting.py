# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    #print(arr)
    if len(arr) < 1:
        return([])
    if min(arr) < 0:
        return('Error, negative numbers not allowed in Count Sort')
    d = dict()
    for key in range(len(arr)):
        if arr[key] in d:
            d[arr[key]] += 1
        else:
            d[arr[key]] = 1
    arr = []
    for i in range(len(d)):
        key = min(d.keys())
        for j in range(d.pop(key)):
            arr.append(key)

    return arr
#print(count_sort([4,6,5,6,3,2,5,3,2,1]))
