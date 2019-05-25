# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
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

myArr = [22, 55, 34, 76, 432, 4322, 41, 1, 3]
myArr2 = [12, 546, 87, 65, 32, 67, 54, 777, 765]

print(merge(myArr, myArr2))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):

    if len(arr) > 1:
        l = merge_sort(arr[0: len(arr) // 2])
        r = merge_sort(arr[len(arr) // 2:])
        arr = merge(l, r)

    return arr

print(merge_sort(myArr))


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
