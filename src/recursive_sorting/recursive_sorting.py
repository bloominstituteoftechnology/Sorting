# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    mi = 0
    while len(arrA) or len(arrB): 
        while len(arrA) > 0 and len(arrB) > 0:
            if arrA[0] <= arrB[0]:
                merged_arr[mi] = arrA[0]
                mi += 1
                arrA = arrA[1:]
            else:
                break

        while len(arrB) > 0 and len(arrA) > 0:
            if arrB[0] <= arrA[0]:
                merged_arr[mi] = arrB[0]
                mi += 1
                arrB = arrB[1:]
            else:
                break 
        if len(arrA) == 0 and len(arrB) > 0:
            for i in range(mi, len(merged_arr)):
                merged_arr[i] = arrB[0]
                arrB = arrB[1:]
        elif len(arrA) > 0 and len(arrB) == 0:
            for i in range(mi, len(merged_arr)):
                merged_arr[i] = arrA[0]
                arrA = arrA[1:]

    return merged_arr
arrA = [1,15,8,10]
arrB = [11, 16, 21, 26]
# print(merge(arrA, arrB))

def merge_sort( arr ):
    if len(arr) < 2:
        return arr
    if len(arr) == 2:
        if arr[0] > arr[1]:
            return [arr[1],arr[0]]
        return arr

    L = len(arr)

    # if len(arr) > 2:
    assert L > 2, f'logic error arr len {len(arr)}'
    n = L // 2
    return merge(merge_sort(arr[0:n]), merge_sort(arr[n:]))
    # p = arr[0]
    # arr = arr[1:]
    # arrl = []
    # arrh = []
    # dc = 1
    # for i in range(0,len(arr)):
    #     if arr[i] < p:
    #         arrl.append(arr[i])
    #     elif arr[i] > p:
    #         arrh.append(arr[i])
    #     else: # equal
    #         dc += 1
    # p = [p] * dc
    # print('checklength', L, dc + len(arrl) + len(arrh))
    # print('p', p, type(p))
    # arr = merge_sort(arrl)
    # arr.extend(p)
    # # print('type arr', type(arr))
    # arr.extend(merge_sort(arrh))
    # return arr

arrB.extend(arrA)
arr = arrB
print('initial arr', arr)
print(merge_sort(arr))


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
