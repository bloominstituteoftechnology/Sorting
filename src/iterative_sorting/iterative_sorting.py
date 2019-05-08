
# TO-DO: Complete the selection_sort() function below 

l = [1, 3, 5, 7, 9, 8, 6, 4, 10, 2]

def selection_sort( arr ):

    # loop through n-1 elements
    # For all indices EXCEPT the last index:
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

        # OR Python magic w/ no temp variable
        # arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr

print("selection sort:")
print(selection_sort(l))

test = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    # keep track of if a swap happened during a pass
    swap_occured = True

    while swap_occured:

        # Swap is false unless the following if-statement is triggered
        swap_occured = False

        for i in range(0, len(arr) - 1):

            current_index = i

            if arr[current_index] > arr[current_index + 1]:
                # Swap
                arr[current_index], arr[current_index + 1] = arr[current_index + 1], arr[current_index]
                
                # Set Boolean to True only if a swap happened during the pass
                swap_occured = True

    return arr

print("bubble sort:")
print(bubble_sort(test))

## Blake's Solution

def bubble_sort_solution( arr ):
    
    # If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.

    swapped = True

    while swapped:
        print("this is from our while loop")
        print(arr)
        swapped = False
        # if the for loop does no swaps, the while loop will stop after the first iteration
        
        # Loop through your array
        # iterate to length minus one b/c we're comparing everything to the element in front
        for i in range(len(arr) - 1):
            # Compare each element to its neighbor
            if arr[i] > arr[i + 1]:
                # if elements in wrong position, swap them
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # If elements in wrong position (relative to each other) swap them
    print("this is from our return statement")
    print(arr)
    return arr

# bubble_sort_solution(test)






# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr