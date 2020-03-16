# TO-DO: Complete the selection_sort() function below

"""Start with current index = 0
For all indices EXCEPT the last index:
a. Loop through elements on right-hand-side of current index
    find the smallest element
b. Swap the element at current index with the smallest element found in above loop
"""

#original question
# def selection_sort(arr):
#     # loop through n-1 elements
#     for i in range(0, len(arr) - 1):
#         cur_index = i
#         smallest_index = cur_index
#         # TO-DO: find next smallest element
#         # (hint, can do in 3 loc)
#
#         # TO-DO: swap
#
#     return arr

def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
# TO-DO: find next smallest element
# (hint, can do in 3 loc)
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                place_holder = arr[smallest_index]


# TO-DO: swap
                # arr[j], arr[place_holder] = arr[place_holder], arr[j]
                '''close! doesnt handle end of arr right?'''

                '''this works'''
                arr[smallest_index] = arr[j]
                arr[j] = place_holder

    return arr


# TO-DO:  implement the Bubble Sort function below
'''Loop through your array
Compare each element to its neighbor
If elements in wrong position (relative to each other, swap them)
If no swaps performed, stop. Else, go back to the element at index 0
repeat step 1.
'''


def bubble_sort(arr):
    #sets up a condition where we can see if there have been changes made
    arr_change = True
    while arr_change :
        # turns off condition while we do our check
        # only turns back on if change made
        # if it stays False, it just returns what was passed in because its already sorted
        arr_change = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i+1] :
                #give i a temp home while we do next step so we dont lose it
                place_holder = arr[i]
                # this is where we set i and i+1 equal to eachother,
                # then we set i+1 equal to i essentially swapping positions
                arr[i]=arr[i+1]
                arr[i+1] = place_holder
                # if there was actually a change, we will set condition back to true
                # if it stays False, it just returns what was passed in because its already sorted
                arr_change = True
    return arr




# I did not originate this code below!, this was aquired for a working example only

# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    print(f'Input: {arr}')
    # Need to define a count list with a maximum passed in, maybe the max of the array
    # Modify the count array to add sums of the previous indexes
    count_list = [0 for x in range(0, maximum)]
    # Loop through the range 0 - maximum
    # Search Arr for all numbers in the index
    # Add the total to count[index]
    for i in range(0, maximum):
        total = 0
        for y in range(0, len(arr)):
            if arr[y] == i:
                total += 1
        count_list[i] = total

    # Need a positional counter to hold change position
    # While Loop while sum of count_list > 0

    current_index = 0
    list_index = 0
    while current_index < maximum:
        if count_list[current_index] > 0:
            arr[list_index] = current_index
            count_list[current_index] -= 1
            list_index += 1
        else:
            current_index += 1
    return arr

print(count_sort([3, 6, 1, 5, 3, 3, 8, 4, 9], 10))