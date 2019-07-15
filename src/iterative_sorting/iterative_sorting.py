# TO-DO: Complete the selection_sort() function below


def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        sort_index = i
        # find next smallest element
        for j in range(i, len(arr)):
            if arr[j] < arr[sort_index]:
                sort_index = j
        # swap
        temp = arr[sort_index]
        arr[sort_index] = arr[i]
        arr[i] = temp
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
#    print("Starting: " + str(arr))
    i = 0
    while i < len(arr) - 1:
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            i = 0 # Start it over
#            print(arr) # uncomment to watch the progression
        else:
            i = i + 1  
#    print("Final: " + str(arr))
    return arr

# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
