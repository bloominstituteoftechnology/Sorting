# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    for i in range(len(arr)-1):
        cur_value = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[cur_value]:
                cur_value = j
        arr[i], arr[cur_value] = arr[cur_value], arr[i]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for x in range(len(arr)-1,0,-1):
        for i in range(x):
            if arr[i]>arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    maxnum = maximum +1
    counter = [0] * maxnum
    for i in arr:
        counter[i] += 1
    
    index = 0;
    for i in range(maxnum):
        for y in range(counter[i]):
            arr[index] = i
            index += 1
    return arr

print(count_sort([2,3,6,1,7,5], 7))

