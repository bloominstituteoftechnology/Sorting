
# 1. Select a pivot. Often times this is the first or last element in a set. It can also be the middle.
# 2. Move all elements smaller than the pivot to the left. 
# 3. Move all elements greater than the pivot to the right.
# 4. While LHS and RHS are greater than 1, repeat steps 1-3 on each side.

def quick_sort(A):
	quick_sort2(A, 0, len(A)-1)

#create a new partition if head, middle and tail of array is not in order
def quick_sort2(A, low, hi):
    if low < hi:
        p = partition(A, low, hi) # if there is more than one item to be sorted, we call teh partition function
        # we define p as pivot
        quick_sort2(A, low, p - 1) # we call function for everythin to left and right of pivot.
        quick_sort2(A, p + 1, hi)
#pick a pivot to partition	
def get_pivot(A, low, hi):
	mid = (hi + low) // 2
	s = sorted([A[low], A[mid], A[hi]]) # returns a sorted list of the specified iterable object.
	if s[1] == A[low]:
		return low
	elif s[1] == A[mid]: # we choose the middle of the index.
		return mid
	return hi
	
def partition(A, low, hi):
	pivotIndex = get_pivot(A, low, hi)
	pivotValue = A[pivotIndex]
	A[pivotIndex], A[low] = A[low], A[pivotIndex] # set our pivot value to the left side of list
	border = low # we set the border to the low index

    #move all elements smaller than the pivote value to left, all elements greater to right
	for i in range(low, hi+1):
		if A[i] < pivotValue: # if the item is less than the pivot value, swap to left side of list
			border += 1
			A[i], A[border] = A[border], A[i]
	A[low], A[border] = A[border], A[low] # swap pivot value, which is our low value into the border position

	return (border)
	

# A = [5,9,1,2,4,8,6,3,7]
# print(A)
# quick_sort(A)
# print(A)

#----------------------------------------------

# arr = [3,0,1,8]

# def quick_sort(arr):
#     # for h in range(0,len(arr)-1):
#     ind = 0
#     while ind != len(arr):
#         for i in range(1, len(arr)):
#             if arr[ind] > arr[i]:
#                 arr[ind], arr[i] = arr[i], arr[ind]
#         ind +=1
#     return arr

# print(quick_sort(arr))
    # new_list = arr
    # first = 0
    # last = len(arr)-1
    # pivot_index = (first + last) // 2
    # new_list_L = new_list[:pivot_index]
    # new_list_R = new_list[pivot_index:]
    # while len(new_list_L) > 1 and len(new_list_R)  > 1:
    #     for j in range(first, last):
    #         if arr[j] <= arr[pivot_index]:
    #             first = first+1
    #             arr[first], arr[j] = arr[j], arr[first]          
    #     arr[first+1], arr[last] = arr[last], arr[first+1]
    #     new_list_L = new_list[:pivot_index-1]
    #     new_list_R = new_list[:pivot_index+1]
   
    # new_list = arr
    # first = 0
    # last = len(new_list)-1
    # pivot_index = (first + last) // 2
    # new_list_L = new_list[:pivot_index]
    # new_list_R = new_list[pivot_index:]
    # while len(new_list_L) > 1 and len(new_list_R)  > 1:
        
    #     for i in range(len(new_list)):
    #         j = i
    #         temp = new_list[i]
    #         while j > -1 and temp > new_list[j-1]
    #             new_list[j] = new_list[j - 1] # Iterate to the left until you 
    #             # find the correct index in the "sorted" part of the array at which this element should be inserted
    #             j -= 1


# TO-DO: complete the help function below to merge 2 sorted arrays
# def merge( arrA, arrB ):
#     elements = len( arrA ) + len( arrB )
#     merged_arr = [0] * elements
#     # TO-DO
    
#     return merged_arr

#----------------------------------------------

# def get_half(arr): 
#     if len(arr) >1: 
#         mid = len(arr)//2 #Finding the mid of the array 
#         L = arr[:mid] # Dividing the array elements  
#         R = arr[mid:] # into 2 halves 
  
#         get_half(L) # Sorting the first half 
#         get_half(R) # Sorting the second half 
  
#         i = j = k = 0
          
#         # Copy data to temp arrays L[] and R[] 
#         while i < len(L) and j < len(R): # while the length of each half is not 0
#             if L[i] < R[j]: # if the first element in the left half is less than the right
#                 arr[k] = L[i] # make the first element of the array be this smaller first element
#                 i+=1
#             else: 
#                 arr[k] = R[j] # if the first element is bigger than the first to the right
#                 # set the right first element as the first element of the array
#                 j+=1
#             k+=1# do this replacement for sorting each item of the left and right halves 
#             # to form a new array, one array index at a time
          
#         # Checking if any element was left 
#         while i < len(L): 
#             arr[k] = L[i] 
#             i+=1
#             k+=1
          
#         while j < len(R): 
#             arr[k] = R[j] 
#             j+=1
#             k+=1

# def get_list(arr):
#     for i in range(len(arr)):         
#         print(arr[i],end=" ") 
#     print() 

# arr = [5,9,1,2,4,8,6,3,7] 
# get_list(arr)
# get_half(arr)
# get_list(arr)

#----------------------------------------------

# l = []
# # # TO-DO: implement the Merge Sort function below USING RECURSION    
# def get_single(arr):
#     if len(arr) == 1:
#         l.append(arr)
#         return
#     else:
#         arr = get_half(arr)
#         get_single(arr)

# # def single_lists(arr):


# arr = [5,9,1,2,4,8,6,3,7] 
# get_single(arr) 
# print(l)


# def find_R(arr):
#     if len(arr) <= 1:
#         return 
#     mid = len(arr)//2
#     arr = arr[mid:]
#     print(arr)
#     # return LHS, RHS
#     find_R(arr)

# def split_arr(arr):
#     arr = find_L(arr)
#     # R = find_R(arr)
#     split_arr(arr)
#     return arr

# def create_list_broken_arrs(LHS, RHS):
#     list_of_single_arrs = []
#     list_of_single_arrs.append(LHS)
#     list_of_single_arrs.append(RHS)
#     return list_of_single_arrs

# def merge_sort(arr):
#     # for i in final_list:
#     #     if len(i) > 1:
#     LHS, RHS = find_L_R(arr)
#     list_of_single_arrs = create_list_broken_arrs(LHS, RHS)
#     for i in list_of_single_arrs:
#         if len(i) > 1:
#             print(i)
#             LHS, RHS = find_L_R(list_of_single_arrs)
#             list_of_single_arr = create_list_broken_arrs(LHS, RHS)   
#             list_of_single_arrs.append(LHS)
#             list_of_single_arrs.append(RHS)
#     return list_of_single_arrs

# def merge_sort_without_breaking(arr):
#     #for each broken up array
#     for i in range(len(arr)-1):
#         if arr[i] > arr[i+1]: 
#             arr[i+1], arr[i] = arr[i], arr[i+1]
#     #stitch array back
#     for i in range(len(arr)-1):
#         l = []
#         l.append(i)
#         l.append(i+1)
#         print(l)
#     return arr




#     return arr


# # STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr

# def merge_sort_in_place(arr, l, r): 
#     # TO-DO

#     return arr


# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort( arr ):

#     return arr



#merge_sort base case, make sure you don't already have an assorted array, so make sure each element is longer than 1
# def merge( arrA, arrB ):
#     elements = len( arrA ) + len( arrB )
#     merged_arr = [0] * elements
#     a = 0#temp standin for i, we use as temporary indices
#     b = 0
#     # arrrA and arrB are sorted compare 1st element of each 
#     for i in range(0, elements):
#         if a >= len(arrA): 
#             merged_arr[i] = arrB[b]
#             b += 1
#         elif b >= len(arrB):
#             merged_arr[i] = arrA[a]
#             a += 1
#         elif arrA[a] < arrB[b]: # if item of the left is smaller to the element to the right, add that left element to the array
#             merged_arr[i] = arrA[a]
#             a += 1 # increment the index that we are working on by 1
#         else:
#             merged_arr[i] = arrB[b]
#             b += 1
#     return merged_arr

def merge(arrA, arrB):
    #compare the first element of each
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    index_arr_a = 0
    index_arr_b = 0
    for i in range(len(merged_arr)):
        #if we are done with arr a default to b
        if index_arr_a >= len(arrA):
            merged_arr[i] = arrB[index_arr_b]
            index_arr_b += 1
        # if we are done with adding all of array b, we default to array a
        elif index_arr_b >= len(arrB):
            merged_arr[i] = arrA[index_arr_a]
            index_arr_a += 1
        # add the smallest to the merged array
        elif arrA[index_arr_a] <= arrB[index_arr_b]:
            merged_arr[i] = arrA[index_arr_a]
            index_arr_a += 1 # iterate the pointer for the smaller value
        else:
            merged_arr[i] = arrB[index_arr_b]
            index_arr_b += 1
    return merged_arr

def merge_sort(arr):
    #if the length of the array is larger than 1
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2 # find middle
        # further divides
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        arr = merge(left, right)# put it back together merging left to right
        return arr

# use recursion by solving the smallest relevant problem. 
# python good for collection of stuff

arr = [5,9,1,2,4,8,6,3,7] 
arr = merge_sort(arr)
print(arr)


# def power(value, exponent):
# X ^ -n == 1 / x ^ n
# if exponent < 0
    # exponent *= -1
    # value = 1/value
    # if exponent == 0:
        # return 1
#     return value * power(value, exponent-1)
# print(power(2, 3))    