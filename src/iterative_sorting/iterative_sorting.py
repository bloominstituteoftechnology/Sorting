# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        # Start at the index number to the left of cur_index
        for j in range(cur_index+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        # The commented-out print lines were used for error testing
        # print('Current index:', cur_index)
        # print('Smallest index:', smallest_index)
        cur_index_element = arr[cur_index]
        smallest_index_element = arr[smallest_index]
        # print('Current index element:', cur_index_element)
        arr[cur_index] = smallest_index_element
        # print('Smallest index element:', smallest_index_element)
        arr[smallest_index] = cur_index_element
        # print(arr)

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # Make a "while" loop so it keeps running until there are no swaps
    swap_occurred = True
    while swap_occurred:
        # count number of swaps
        swaps = 0
        # We check the current element and the one to its right.
        # The last element has no element to its right, so let's ignore it.
        for i in range(len(arr)-1):
            cur_index = i
            next_index = i+1
            cur_index_element = arr[cur_index]
            next_index_element = arr[next_index]
            # If the current element is bigger, swap them
            if cur_index_element > next_index_element:
                arr[cur_index] = next_index_element
                arr[next_index] = cur_index_element
                # count swaps
                swaps += 1
        # If there were no swaps, end the loop
        if swaps == 0:
            swap_occurred = False

    return arr


# STRETCH: implement the Count Sort function below
# I used this website: https://www.geeksforgeeks.org/counting-sort/ (pseudo-code only)
# and this video: https://www.youtube.com/watch?v=7zuGmKfUt7s
# for information on Count Sort
def count_sort( arr, maximum=-1 ):
    # Get maximum value
    if maximum == -1:
        # max() function requires a non-empty array,
        # so when array is empty, set max to 0
        if len(arr) == 0:
            maximum = 0
        else:
            maximum = max(arr)
    # Create count_array. Its length needs to be 1 more than the max value,
    # since e.g. if the max value is 10, I need the count_array to end at position
    # 10, and since Python indexing starts at 0, this means it needs a length of 11.
    count_array = [0] * (maximum + 1)
    # Track if input array has a negative value
    negative_value_exists = False
    for val in arr:
        if val < 0:
            # If there's a negative value, end loop immediately
            # and make an error message.
            negative_value_exists = True
            arr = "Error, negative numbers not allowed in Count Sort"
            break
        # Otherwise, keep track of the value counts
        count_array[val] += 1
    # Commented-out print statement was used for bug fixing
    # print(count_array)
    for i in range(1, len(count_array)):
        # Now, change count_array so its counts are cumulative
        cumulative_count = count_array[i] + count_array[i-1]
        count_array[i] = cumulative_count
    # Finally, since Python indexing starts at 0, we need to subtract
    # everything by 1 so that the numbers end up at the right index value.
    for i in range(len(count_array)):
        count_array[i] -= 1
    # print(count_array)
    new_array = [-1] * len(arr)
    # Use count_array to place elements in order
    for val in arr:
        # No need to do anything if there's a negative value
        if negative_value_exists:
            break
        val_count = count_array[val]
        # Place value in the position assigned by count_array
        new_array[val_count] = val
        # Subtract relevant count_array value by 1
        count_array[val] -= 1

    # Only return new_array if there are no negative values
    if negative_value_exists is False:
        arr = new_array

    return arr