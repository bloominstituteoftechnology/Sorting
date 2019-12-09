# TO-DO: Complete the selection_sort() function below

##find the smallest item and swap into the sorted partition
### separated into sorted and unsorted
## you progress the array looking for a smaller number
## if you find a smaller number, you swap it with min and it becomes the new minimum

#[5,2,1,9,0,4,6]
# ^ <--------->
# |         |
# sorted   unsorted

# 4 is the minimum right now
# we will compare it to every number to its right
# as soon as we come across a number that is lower than the current minimum,
# we assign it as the new minimum and continue on
# at the end of the iteration,  the new min value from the unsorted list
# will be moved to the left as the last value of the sorted list
# process will repeat until list is fully sorted

def selection_sort( arr ):
    index_length = range(0, len(arr)-1)

    for i in index_length:
	## each time we do an iteration we want that
	## first element in the unsorted list to be the
	## the default min
	## need this default to do the comparisons && swaps

        min_value = i

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
        ## i + 1 being RHS

            if arr[min_value] > arr[j]:
            ## going through all the elements to the right
			## of where we currently are on the index and if
			## and if we find something smaller,
			## change that to the min value

                min_value = j

        arr[i], arr[min_value] = arr[min_value], arr[i]
        ## performs the swap
        # TO-DO: swap

    return arr
print(selection_sort([5,2,1,9,0,4,6]))



#################################################################################




# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    ##get length to help make code readability better
    ##we subtract 1 from length because we are always comparing current val with next val
    arrLength = len(arr) -1

    # number of rounds will be total length -1 so if length is 7, we will do 6 rounds
    for i in range(arrLength):

        # at each round, we compare the current j with the next value
        for j in range(arrLength - i):

            # only swap positions if left val > right val
            # we are trying to get smallest starting left and work our way right
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j +1], arr[j]
    return arr
print(bubble_sort([5,2,1,9,0,4,6]))



# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr