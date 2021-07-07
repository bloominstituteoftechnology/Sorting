# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )

    # TO-DO
    a = 0
    b = 0
    minLen = min(len(arrA), len(arrB))
    merged_arr = [0] * (minLen*2 - 1)

    longerArr: list
    if len(arrA) > len(arrB):
        longerArr = arrA
    else:
        longerArr = arrB

    for i in range(0, (minLen*2)-1):
        print(f"arra[a] = {arrA[a]}")
        print(f"arrb[b] = {arrB[b]}")
        print(f'count = {i}')
        if arrA[a] <= arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1
    merged_arr += longerArr[(minLen)-1:]
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) == 0 or len(arr) == 1:
        return arr
    else:
        middle = len(arr)//2
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])

        return merge(left,right)


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
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr2 = []
arr3 = [2]
arr4 = [0, 1, 2, 3, 4, 5]
arr5 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

#print(merge(arr1, arr4))
#print(merge([0], [1]))

#print(merge_sort([0,1]))
print(merge_sort(arr5))