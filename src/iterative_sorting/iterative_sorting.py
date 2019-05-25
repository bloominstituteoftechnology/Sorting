# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j   

        # TO-DO: swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp



    return arr
l = [12, 19, 7, 8, 17, 15, 32, 0, 9, 7, 4, 7, 8, 15, 6, 12, 7, 8, 8, 20, 3, 11]

print(selection_sort(l))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swap_occured = True
    while swap_occured:
        for i in range(len(arr)):
            for j in range(0, len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                     # TO-DO: swap
                    temp = arr[j + 1]
                    arr[j + 1] = arr[j]
                    arr[j] = temp
        else: 
                swap_occured = False

    return arr

def bubble_sort1(arr):
    swapped = True
    while swapped:
        print("this is from our while loop")
        print(arr)
        swapped = False
        # if the for loop does no swaps, the while loop will stop after the first iteration
        # iterate to length minus one because we're comparing everything to the element in front
        # Loop through your array
        for i in range(len(arr) - 1):
            # Compare each element to its neighbor
            if arr[i] > arr[i + 1]:
                # If elements in wrong position (relative to each other, swap them)
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        # If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.
    print("this is from our return statement")
    print(arr)
    return arr

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

print(bubble_sort1(arr1))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum = -1 ):

    return arr