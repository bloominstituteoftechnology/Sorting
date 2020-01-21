# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = []
    # TO-DO
    i = j = 0
    while elements > 0:  
        if i >= len(arrA):
            merged_arr.append(arrB[j])
            j += 1
        elif j >= len(arrB):
            merged_arr.append(arrA[i])
            i += 1
        elif arrA[i] < arrB[j]:
            merged_arr.append(arrA[i])
            i += 1
        else:
            merged_arr.append(arrB[j])
            j += 1
        elements -= 1
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) == 1 or arr == []:
        #print(f'exiting merge sort, {arr}')
        return arr

    #print(f'inside merge_sort arr = {arr}')
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
    #arr = merge(merge_sort(arr1), merge_sort(arr2))

print(merge_sort([4, 6, 2, 3, 1, 5]))

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
