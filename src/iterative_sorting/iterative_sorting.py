
# TO-DO: Complete the selection_sort() function below 

l = [1, 3, 5, 7, 9, 8, 6, 4, 10, 2]

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        # Loop through each index from the current through the end of the array
        for each_index in range(cur_index, len(arr)):

            # If the _element_ at the index in the array we are looking at
            # is smaller than the _element_ in the index holding the smallest...
            if arr[each_index] < arr[smallest_index]:

                # ... set the actual index of the smallest to the index
                # we are looking at
                smallest_index = each_index 

        # TO-DO: swap

        # set a temp variable that holds the element at the index of the smallest
        temp = arr[smallest_index]

        # set the element in the smallest_index to the element
        # that's in the current index
        arr[smallest_index] = arr[cur_index]

        # set the element at the current index to the temporary var,
        # which is the smallest element
        arr[cur_index] = temp

    return arr

print(selection_sort(l))

test = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    # keep track of if a swap happened during a pass
    swap_occured = True

    current_index = 0

    while swap_occured:

        for i in range(0, len(arr) - 2):

            if arr[current_index] > arr[current_index + 1]:
                # Swap
                temp = arr[current_index]
                arr[current_index] = arr[current_index + 1]
                arr[current_index + 1] = temp
                swap_occured = True
            else:
                swap_occured = False
            
            current_index += 1

    return arr

print(bubble_sort(test))


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr