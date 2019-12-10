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

            if arr[j] < arr[min_value]:
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
	index_length = len(arr) - 1
	#setting a variable name to length needed
	## - 1 used here because we cannot perform a comparison on the last number of the list
	## because there isn't a number after it
	sorted = False
	##local variable == use to break us out when list is sorted
	## no forever loop yay!

	while not sorted:
	## need to perform at a number of iterations we don't know
	## as long as sorted  is false, will perform these actions
		sorted = True
		##reference local variable
		for i in range(0, index_length):
		##comparison time
			if arr[i] > arr[i+1]:
			# if value to left is greater than the value to the right
				sorted = False
				##sorted will be false
				arr[i], arr[i+1] = arr[i+1], arr[i]
				##swap the two values in our list


				## whenever we sort all the values in our list,
				##if statement wont activate
				## sorted will turn true and break out of iteration loop

	return arr
print(bubble_sort([5,2,1,9,0,4,6]))



# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr