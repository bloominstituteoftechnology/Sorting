# TO-DO: complete the helpe function below to merge 2 sorted arrays
## sort left half of array assuming n > 1
## sort right half of array assuming n > 1
## merge the two halves together

## making subarrays to break down problem into bits



def merge( arrLeft, arrRight ):
    merged_arr = []
    ##create a new merged list
    ## final output array
    ## will return it at the end


    # TO-DO
    ## cool note plural form of index is indices

    # variables to hold current indices
    left_index, right_index = 0,0

    while left_index < len(arrLeft) and right_index < len(arrRight):
    #turn into while look where we will continue iterating until we have used up all
    ## the elements in one of the input lists

    	if arrLeft[left_index] < arrRight[right_index]:
    	# on each of the iterations we compare the elements seen at the top of each list and

    		merged_arr.append(arrLeft[left_index])
    		# and append whichever is smaller onto our merged_arr

    		left_index += 1
    		## afterwards we also increment the index for the list we pulled from
    		## to prevent writing the same element onto the merged_arr again

    	else:

    		merged_arr.append(arrRight[right_index])
    		# and append whichever is smaller onto our merged_arr

    		right_index +=1
    		## afterwards we also increment the index for the list we pulled from
    		## to prevent writing the same element onto the merged_arr again

    if left_index == len(arrLeft):
    # at end of while loop we extend the merged list with whichever of the two
    ## input lists wasn't completely used up inside the while loop

    ## if left_index  === length of arrLeft, we know we pushed all the elements of arrLeft
    ## onto merged_arr

    	merged_arr.extend(arrRight[right_index:])
    	# could be left over elements in arrRight so we push the remaining elements
    	## of arrRight onto merged_arr

    else:
    	merged_arr.extend(arrLeft[left_index:])
    	# could be left over elements in arrLeft so we push the remaining elements
    	## of arrLeft onto merged_arr

    return merged_arr


def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
    	return arr
    else:
	    mid = int(len(arr) // 2)
	    leftArr = merge_sort(arr[:mid])
	    rightArr = merge_sort(arr[mid:])
	    arr = merge(leftArr, rightArr)
    return arr

print(merge_sort([5,2,6,9,1,3,8]))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
