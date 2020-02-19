# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    a = 0
    b = 0
    c = 0

    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            merged_arr[c] = arrA[a]
            a =  a + 1
            c = c + 1      
        else:
            merged_arr[c] = arrB[b]
            b =  b + 1
            c = c + 1       

    while a < len(arrA):
        merged_arr[c] = arrA[a]
        c = c + 1
        a = a + 1
    while b < len(arrB):
        merged_arr[c] = arrB[b]
        c = c + 1
        b = b + 1
    
    # print(merged_arr)
    return merged_arr

# merge([1, 3, 5, 7], [2, 4, 6, 8])
# TO-DO: implement the Merge Sort function below USING RECURSION

# import math
# def merge_sort( arr ):
#     # TO-DO
#     print(arr)
#     if len(arr) < 2:
#         return arr
    
#     half_point = math.ceil(len(arr) / 2)
#     # size = len(arr)

#     h1 = [0] * half_point
#     h2 = []

#     for i in range(0, len(arr)):
#         if (i < half_point):
#             h1[i] = arr[i]
#         else:
#             h2.append(arr[i])
    
#     # for k in range(half_point, len(arr)):
#     #     h2[k] = arr[k]
    
#     h1 = merge_sort(h1)
#     h2 = merge_sort(h2)

#     arr = merge(h1, h2)

#     return arr

# merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])

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
