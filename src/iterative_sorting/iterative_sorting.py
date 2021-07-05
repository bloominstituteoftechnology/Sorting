from random import shuffle
nums = [n for n in range(10)]
shuffle(nums)

# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # go through list
    for i in range(0, len(arr) - 1):
        min_index = i #smallest item in unsorted area
        for curr_index in range(i+1, len(arr)): #for every item in unsorted
            if arr[min_index]>arr[curr_index]: #check if item is smaller than current min
              min_index = curr_index #and assign that index as new min
#swap min with first item of the unsorted 
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return selection_sort(nums)
print(selection_sort)


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    n = len(arr)
#go through all of the array items
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] : #if left is bigger than right swap 
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr