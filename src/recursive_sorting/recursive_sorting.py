def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    a = 0
    b = 0
    for i in range(0, elements):
        if a >= len(arrA):
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
    return merged_arr

def merge_sort(arr):
    if len(arr) > 1:
        left = merge_sort(arr[0:int(len(arr) / 2)])
        right = merge_sort(arr[int(len(arr) / 2):])
        arr = merge(left, right)
    return arr
# def merge(arrA, arrB):
#     elements = len(arrA) + len(arrB)
#     merged_arr = [0] * elements
#     # TO-DO
#     a = 0
#     b = 0
#
#     for i in range(0, elements):
#         if a >= len(arrA):
#             merged_arr[i] = arrB[b]
#             b += 1
#         elif b >= len(arrB):
#             merged_arr[i] = arrA[a]
#             a += 1
#         elif arrA[a] < arrB[b]:
#             merged_arr[i] = arrA[a]
#             a += 1
#         else:
#             merged_arr[i] = arrB[b]
#             b += 1
#     return merged_arr
#
# def merge_sort(arr):
#     if len(arr) > 1:
#         left = merge_sort(arr[0:int(len(arr) / 2)])
#         right = merge_sort(arr[int(len(arr) / 2):])
#         arr = merge(left, right)
#     return arr 



# TO-DO: complete the helper function below to merge 2 sorted arrays
# problem:
# goal:

# def merge( arrA, arrB ):
#     elements = len( arrA ) + len( arrB )
#     merged_arr = [0] * elements
#     print('here')

    # TO-DO
    # for i in range(len(merged_arr)):
    #     for j in range(len(merged_arr)-(i+1)):
    #         if merged_arr > merged_arr[j+1]:
    #             merged_arr[j], merged_arr[j+1]= merged_arr[j+1], merged_arr[j]


#     return merged_arr
# a = [1,2,3]
# b = [4,5,6]
# print('function call')
# print(merge(a, b))
# TO-DO: implement the Merge Sort function below USING RECURSION
# def merge_sort( arr ):
    # TO-DO
    # for j in range(len(merged_arr) - (i + 1)):
    #     if merged_arr > merged_arr[j + 1]:
    #         merged_arr[j], merged_arr[j + 1] = merged_arr[j + 1], merged_arr[j]

    # return arr


# STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO
#
#     return arr

# def merge_sort_in_place(arr, l, r):
#     # TO-DO
#
#     return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort( arr ):
#
#     return arr
