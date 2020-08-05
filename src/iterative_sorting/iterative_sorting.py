# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(1, len(arr)):
        for j in range (i-1,-1,-1):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
            else:
                break
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    while True == True:
        didSwap = False
        for i in range(1,len(arr)):
            if arr[i-1] > arr[i]:
                temp = arr[i]
                arr[i] = arr[i-1]
                arr[i-1] = temp
                didSwap = True
        if didSwap == False:
            break
    return arr

# STRETCH: implement the Count Sort function below
#def count_sort( arr, maximum=-1 ):
#    newArr = [0] * maximum
#    for i in arr:

 #   return arr