# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    cA, cB, cM = 0,0,0
    
    while(cA < len(arrA) and cB < len(arrB)):
        if(arrA[cA] < arrB[cB]):
            merged_arr[cM] = arrA[cA]
            cA += 1
        else:
            merged_arr[cM] = arrB[cB]
            cB += 1
        cM += 1
    
    if(cA < len(arrA)):
        while(cM < len(merged_arr)):
            merged_arr[cM] = arrA[cA]
            cM +=1
            cA +=1

    if(cB < len(arrB)):
        while(cM < len(merged_arr)):
            merged_arr[cM] = arrB[cB]
            cM +=1
            cB +=1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if(len(arr) <= 1):
        return arr
    else:
        half = len(arr) // 2
        arr1 = arr[half:]
        arr2 = arr[:half]

        sorted_1 = merge_sort(arr1)
        sorted_2 = merge_sort(arr2)

        return merge(sorted_1, sorted_2)

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    for i in range(start, end):
        for x in range(start, end):
            if(arr[x] > arr[x+1]):
                t = arr[x]
                arr[x] = arr[x+1]
                arr[x+1] = t
    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO
    m = (l+r)//2
    if(r <= l):
        return arr
    
    merge_sort_in_place(arr, l, m)
    merge_sort_in_place(arr, m+1, r)

    merge_in_place(arr, l, m, r)
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
