# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    a = 0
    b = 0 
    for i in range(elements):
        if a == len(arrA):                  
            merged_arr[i:] = arrB[b:]    
            break
        if b == len(arrB):                  
            merged_arr[i:] = arrA[a:]       
            break
                                            
        if arrA[a] <= arrB[b]:              
            merged_arr[i] = arrA[a]
            a += 1                          
        else:
            merged_arr[i] = arrB[b]         
            b += 1                          
    return merged_arr
# print(merge([2, 3, 4, 6, 8, 8], [3, 7, 9]))
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):    # TO-DO
    arr_len = len(arr)                       
    if arr_len == 1 or arr_len == 0:          
        return arr                          
    breakIndex = (arr_len//2)       
    leftArray = merge_sort(arr[breakIndex:])                          
    rightArray = merge_sort(arr[:breakIndex])     
    return merge(leftArray, rightArray)     

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
