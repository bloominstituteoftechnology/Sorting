# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    a = 0 # initial array [1 4 9 10]
    b = 0 # initial array [ 2 3 6 7 8]
    # put both element list in one array [1 2 3 4 6 7 8 9 10]
    # arrA & arrB are sorted , we might need to compare the first element of each list before merging!
    # Therefore:
    for el in range(0, elements):# for every element in range from (0 to elements)
        if a >= len(arrA):#     
            merged_arr[el] = arrB[b]
            b += 1
        elif b >= len(arrB):  
            merged_arr[el] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:  
            merged_arr[el] = arrA[a]
            a += 1
        else:  
            merged_arr[el] = arrB[b]
            b += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # base case
    if len(arr) >1: 
        left = merge_sort(arr[0:len(arr) // 2]) # Dividing the array elements  
        right = merge_sort(arr[len(arr) // 2:]) # into 2 lists
        arr = merge(merge_sort(left), merge_sort(right))
    return arr


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
