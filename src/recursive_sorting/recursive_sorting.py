# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    
    for i in range(len(merged_arr)):
    
        if len(arrA) > 0 and len(arrB) > 0:
            # arryA[0] is smaller, add it to merged_arr and delete from arrA
            if arrA[0] < arrB[0]:
                merged_arr[i] = arrA[0]
                arrA.remove(arrA[0])
            else:
            # arryB[0] is smaller, add it to merged_arr and delete from arrB     
                merged_arr[i] = arrB[0]
                arrB.remove(arrB[0])
        else:
            # lenght of ArrA is equal to 0 merged_arr = arrB remove arrB. Else: merged_arr = arrA remove ArrA
            if len(arrA) == 0:
                merged_arr[i] = arrB[0]
                arrB.remove(arrB[0])
            else:   
                merged_arr[i] = arrA[0]
                arrA.remove(arrA[0]) 
             
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    
    if len(arr) > 1:
        # divide list (array) and assign each half
            middle = len(arr)//2
            l, r = merge_sort(arr[:middle]), merge_sort(arr[middle:])
            arr = merge(l, r)
    
    return arr


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
