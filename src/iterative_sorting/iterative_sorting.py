# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        min_index = i
        for j in range (i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]





    return arr

# print(selection_sort([3,4,2,9,28]))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    x = len(arr)

    for i in range (x):
        for j in range(0, x-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
            
print(bubble_sort([4,5,39,34,22]))
