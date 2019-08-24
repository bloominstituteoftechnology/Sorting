# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    i_left = i_right = 0
    elements = len( arrA ) + len( arrB )
    merged_arr = []
    target_arr_len = [0] * elements
    # TO-O
    if len(arrA) == 0:
        return arrA
    elif len(arrB) == 0:
        return arrB

    while len(merged_arr) < len(target_arr_len): 
        if arrA[i_left] <= arrB[i_right]:
            merged_arr.append(arrA[i_left])
            i_left += 1
        else:
            merged_arr.append(arrB[i_right])
            i_right += 1

        if i_right == len(arrB):
            merged_arr += arrA[i_left:]
            break
        elif i_left == len(arrA):
            merged_arr += arrB[i_right:]
            break
            
    
    print(merged_arr)
    return merged_arr

def split(i_list):
    i_list_len = len(i_list)
    midpoint = i_list_len // 2
    print i_list[:midpoint], i_list[midpoint:]
    return i_list[:midpoint], i_list[midpoint:]

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr
    else:
        left, right = split(arr)
        return merge(merge_sort(left), merge_sort(right))

    # return arr


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




the_list = [1,3,5,9156,256,45,4,7]
# left_list = split(the_list)[0]
# right_list = split(the_list)[1]
#
# merge(left_list, right_list)

merge_sort(the_list)

