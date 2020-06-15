# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    # we are looping through each item in our collection one at a time
    # 0 is the starting number of the index
    # we say -1 here as we have only one item in the list we dont want to do a comparison
    # instead we can assume that is the highest value as it it the last one
    for i in range(0, len(arr) - 1):
        # taking in account the smallest element comparing with the largest on
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        # so all elements to the right of the position (cur_index = i)
        for j in range(i+1, len(arr)):
            # if arr in the position j is less than our smallest_index
             if arr[j] < arr[smallest_index]:
                # then we need to replace our smallest_index with j
                # so we going through all the elements to the right we are currently are 
               smallest_index = j
             
        # TO-DO: swap
        # at the end before our loop we swap the element located in the current index 
        # with the smallest item we locate during our loop
        # if we found an item which is smaller than the smallest index than our default the we need to swap the items
        if smallest_index != i:
            arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr


# TO-DO:  implement the Bubble Sort function below
# takes an unsorted list and orders it to sign in values 
# so we have the lowest in the begining and the highest number will be at the end of our list
# we comparing the highest values together and moving the highest to the right
# we repeat the comparison in every iteration so every highest value will be at the right side
# we continue looping at this list until all numbers will be sorted
# when we sort all our items we need to create a way to break the iterations

def bubble_sort( arr ):
    # we need the indexing_length were we are going to make the comparison
    # we say -1 because we cant compare with a number of the list if there is no number there
    indexing_length = len(arr)-1
    # we use a local variable for this function
    # we using the sorted variable to a control to break us out whenever the list is been sorted
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            # so if arr position i to the left is greater than the arr to the position to the right 
            if arr[i] > arr[i+1]:
                # this sorted variable is false
                sorted = False
                # we need to flip these two values in our list
                arr[i], arr[i+1] = arr[i+1], arr[i]
                # so in the end if statement will activate and the sorted variable will remain true
                # and that will break us out the while loop
    return arr

print(bubble_sort([3,5,7,9]))


# STRETCH: smallest_index
def count_sort( arr, maximum=-1 ):

    return arr