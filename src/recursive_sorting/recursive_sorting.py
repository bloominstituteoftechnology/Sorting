# TO-DO: complete the helpe function below to merge 2 sorted arrays

arrA = [1, 5, 7, 15]
arrB = [3, 8, 10]
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    a = b = 0
    
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
    
print(merge(arrA, arrB ))

arr = [6,4,99,5,2,87,90, 3, 7, 32, 54, 55]
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr
    left = arr[:len(arr)// 2]
    right = arr[len(arr)// 2 :]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)
    
print(merge_sort( arr ))

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

# TO-DO: implement the Merge Sort function below USING RECURSION

