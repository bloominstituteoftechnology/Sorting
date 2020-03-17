# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    # print(elements)
    merged_arr = [0] * elements
    # TO-DO
    i_a = 0
    i_b = 0

    for i in range(elements):
        # print(f'i {i}')
        # print('t', merged_arr[i:])
        # print('g', arrB[i_b:])
        if i_a >= len(arrA):
            merged_arr[i] = arrB[i_b]
            i_b += 1
        elif i_b >= len(arrB):
            merged_arr[i] = arrA[i_a]
            i_a += 1
        elif arrA[i_a] < arrB[i_b]:
            merged_arr[i] = arrA[i_a]
            i_a += 1
        else:
            merged_arr[i] = arrB[i_b]
            i_b += 1
 
    return merged_arr

arrA = [4, 2, 5, 1] 
arrB = [6, 9, 8, 20]
print(f'merge {merge(arrA, arrB)}')
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # print(arr)
    if len(arr) <= 1:
        return arr
    mid= len(arr) // 2
    print (mid)
    right = arr[:mid]
    left = arr[mid:]
    

    
    return merge(merge_sort(right), merge_sort(left))


print(f' merge sorted {merge_sort(merge(arrA, arrB))}')
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
