# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) > 1:
        splitindex = len(arr) // 2
        arrA = arr[:splitindex]
        arrB = arr[splitindex:]
        merge_sort(arrA)
        merge_sort(arrB)
    
        a,b,i = 0,0,0
        while a < len(arrA) and b < len(arrB):
            if arrA[a] < arrB[b]:
                arr[i] = arrA[a]
                a += 1
            else:
                arr[i] = arrB[b]
                b += 1
            i += 1

        while a < len(arrA):
            arr[i] = arrA[a]
            i += 1
            a += 1

        while b < len(arrB):
            arr[i]=arrB[b]
            i += 1
            b += 1

    return arr

print(merge_sort([2,1,5,4,3]))
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
