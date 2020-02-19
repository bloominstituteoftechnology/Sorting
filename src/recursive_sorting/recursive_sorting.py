
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
	

A = [5,9,1,2,4,8,6,3,7]
print(A)
quick_sort(A)
print(A)


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
def get_half(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        get_half(L) # Sorting the first half 
        get_half(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): # while the length of each half is not 0
            if L[i] < R[j]: # if the first element in the left half is less than the right
                arr[k] = L[i] # make the first element of the array be this smaller first element
                i+=1
            else: 
                arr[k] = R[j] # if the first element is bigger than the first to the right
                # set the right first element as the first element of the array
                j+=1
            k+=1# do this replacement for sorting each item of the left and right halves 
            # to form a new array, one array index at a time
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1

def get_list(arr):
    for i in range(len(arr)):         
        print(arr[i],end=" ") 
    print() 

arr = [5,9,1,2,4,8,6,3,7] 
get_list(arr)
get_half(arr)
get_list(arr)

#     return arr

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
