# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    # print(f"elements {elements}")
    merged_arr = []
    # TO-DO
    # print(f"arrA: {arrA}, arrB: {arrB}")
    # print(arrA[0], arrB[0])

    if arrA < arrB:
        merged_arr = merged_arr.append(arrA)

    print(merged_arr)

    return merged_arr



# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        # print(arr)
        return arr

    arrA = merge_sort(arr[:len(arr)//2])
    # print(arrA)
    arrB = merge_sort(arr[len(arr)//2:])
    # print(arrB)


    return merge(arrA, arrB)

#     def merge_sort( arr ):
# 	# TO-DO
# 	if len(arr) <= 1:
# 		return arr
# ​
# 	arrA = merge_sort(arr[:len(arr)//2]) #[0] 
# 	arrB = merge_sort(arr[len(arr)//2:]) # [9]
# ​
# 	return merge(arrA,arrB)

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

merge_sort(arr1)

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
