# TO-DO: complete the helpe function below to merge 2 sorted arrays
# a = [1,3,5] 
# b = [2,4,6]
# merged_arr= [1, 2, 0, 0, 0, 0]
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO

    #initialize pointers to first element of both arrays
    a = 0 # these are indexes
    b = 0
    #compare arr[0] of arrA and arrB
    for i in range(elements):
        if a >= len(arrA):
            print(i)
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1


    #copy the smallest to merged_arr
    
    return merged_arr

    


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # base case - if len(arr) == 1, return arr
    if len(arr) <= 1:
        return arr

    #split arr in half
    left = arr[:len(arr) // 2]
    right = arr[len(arr) // 2:] #trouble understanding this slice

    #sort each half
    left = merge_sort(left)
    right = merge_sort(right)

    #merge them back together
    #return arr
    return merge(left, right)


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
