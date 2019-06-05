# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    
    if len(arrA) == 0:
        return arrB
    if len(arrB) == 0:
        return arrA
    
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements

    x, y = 0, 0
    for i in range(elements):
        if len(arrA) == x:
            for j in range(y, len(arrB)):
                merged_arr[i + j - y] = arrB[j]
            return merged_arr
        elif len(arrB) == y:
            for j in range(x, len(arrA)):
                merged_arr[i + j - x] = arrA[j]
            return merged_arr

        if arrA[x] < arrB[y]:
            merged_arr[i] = arrA[x]
            x += 1
        else:
            merged_arr[i] = arrB[y]
            y += 1
    
    return merged_arr



# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) <= 1:
            return arr

    split = len(arr) // 2
    return merge(merge_sort(arr[:split]), merge_sort(arr[split:]))


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
