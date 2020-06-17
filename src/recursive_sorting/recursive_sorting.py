# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # print(arrA, arrB)

    merged_arr = []# * elements
    i,j =0,0
    while i< len(arrA) and j<len(arrB):
        if arrA[i]< arrB[j]:
            merged_arr.append(arrA[i])
            i += 1
        else:
            merged_arr.append(arrB[j])
            j += 1

    merged_arr = merged_arr+arrA[i:]#if any element is left out strating from i till the end of the arrayA
    merged_arr= merged_arr+arrB[j:] # if any element is left out strating from j till the end of the arrayB

    # TO-DO

    # print (merged_arr)
    return merge d_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr)<=1:
        return arr
    mid= len(arr)//2
    arrA = merge_sort(arr[:mid])#one element less than mid
    arrB =  merge_sort(arr[mid:])#start from mid till the end
    arr = merge( arrA , arrB)
    # TO-DO

    return arr
list= [7,5,9,2,3,1]
print(merge_sort(list))
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
