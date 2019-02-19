# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO:  swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):
    # Starting at index 1
    for i in range(1, len(arr)):
        # create a copy of i to not mess up the index
        first = i
        # holds are temp variable which will be put in the place it belongs
        temp = arr[first]
        # while temp is less than our array at the index before temp
        while first > 0 and temp < arr[first-1]:
            # move the item over one
            arr[first] = arr[first-1]
            # move the item all the way to the left place
            first = first-1
        # perform the swap
        arr[first] = temp

    return arr


arr = [2,5,9,7,4,1,3,8,6]
print(arr)
arr = insertion_sort( arr )
print(arr)

def insertion_sort2(arr):
    for i in range(1, len(arr)):
        current_element = arr[i]
        j = i - 1
        while j >= 0 and current_element < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = current_element
    return arr

arr = [2,5,9,7,4,1,3,8,6]
print(arr)
arr = insertion_sort2( arr )
print(arr)
# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(arr) -1):
            if arr[i] > arr[i+1]:
                #swap elements
                arr[i], arr[i+1] = arr[i+1], arr[i]
                # set is_sorted back to false
                is_sorted = False

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr