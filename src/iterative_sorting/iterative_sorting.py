import random
# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for cur_index in range(0, len(arr)-1):
        smallest_index = cur_index

        for select in range(cur_index, len(arr)):
            if arr[select] < arr[smallest_index]:
                smallest_index = select

        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    sorted = False
    while not sorted:
        swaps = 0
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i+1]:
                swaps += 1
                arr.insert(i+1, arr.pop(i))
                print(arr)
        if swaps == 0:
            sorted = True
    return arr


# STRETCH: implement the Count Sort function below


print(bubble_sort(random.sample(range(30), 10)))



def count_sort(arr, maximum=-1):

    return arr
