# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    print("I ran: ", arrA, arrB, "\n")
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    i, j, k = 0,0,0
    print("current merge: ", merged_arr)
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            print("a is smaller b and merge is: ", merged_arr)
            i += 1
        else:
            merged_arr[k] = arrB[j]
            print("b is smaller a")
            j += 1
        k += 1
    
    while i < len(arrA):
        merged_arr[k] = arrA[i]
        print("what is left", merged_arr)
        i += 1
        k += 1
        print(f"after I -- I : {i}, J : {j}, K : {k}")
    while j < len(arrB):
        merged_arr[k] = arrB[j]
        print("what is left", merged_arr)
        j += 1
        k += 1
        print(f"after J -- I : {i}, J : {j}, K : {k}")
    print(f"before return -- I : {i}, J : {j}, K : {k}")
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        half = len(arr) // 2
        left = arr[:half]
        right = arr[half:]
        print("left: ", left, "right: ", right)
        if len(left) > 1:
            merge_sort(left)
        if len(right) > 1:
            merge_sort(right)
    merge(left, right)
    print("last array: ", arr)
    # return arr
merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])

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
