# TO-DO: Complete the selection_sort() function below
# selection sort moves items to left from the right and only continues its sort on the unsorted right side


def selection_sort(arr):
    for i in range(len(arr)):
        lowest_value_index = i
        # for every ele(j) to the right of i
        for j in range(i + 1, len(arr)):
            # search through all ele to the right and move them to the left
            if arr[j] < arr[lowest_value_index]:
                lowest_value_index = j

        arr[i], arr[lowest_value_index] = arr[lowest_value_index], arr[i]

    return arr


random_list_of_arrs = [12, 8, 3, 20, 11]
selection_sort(random_list_of_arrs)
print(random_list_of_arrs)


# TO-DO:  implement the Bubble Sort function below

def bubble_sort(arr):
    # assures you sort through the whole list by negative indexing from end of list
    indexing_measure = len(arr) - 1
    # sorting variable tells loop to run or break out while sorted is false we "run the function"
    sorted = False
    while not sorted:
        # below sorted variable breaks us out of the while loop when the conditional on line 39 is no longer truthy
        sorted = True
        for i in range(0, indexing_measure):
            # if an item on left is greater than the item to the right, set sorted to false and flip those items
            if arr[i] > arr[i + 1]:
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
    # returns the sorted list
    return arr


random_list_of_arr = [5, 2, 1, 8, 4]
bubble_sort(random_list_of_arr)
print(random_list_of_arr)


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
