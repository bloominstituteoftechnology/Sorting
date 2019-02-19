# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        current_index = i;
        smallest_index = current_index;
        #find next smallest element
        for j in range(current_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        #swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[current_index]
        arr[current_index] = temp
    return arr


print(selection_sort([-2, 7, 3, -9, 5, 1, 0, 4, -6]))

# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)):
            if(arr[i] < arr[j]):
                arr[i], arr[j] = arr[j], arr[i] # lots of swaps happen in insertion sort
    return arr

print(insertion_sort([-2, 7, 3, -9, 5, 1, 0, 4, -6]))


# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):
    for k in range(0, len(arr)):
        for i in range(0, len(arr)-k-1):
            if(arr[i] > arr[i+1]): # bubble the largest number to the end of the array and repeat until it's done for all elements in the array, no need to check the largest numbers at the end of the array since the largest numbers are already sorted, so we do n-k-1
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

print(bubble_sort([-2, 7, 3, -9, 5, 1, 0, 4, -6]))


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr