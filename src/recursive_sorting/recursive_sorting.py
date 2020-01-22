# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    
    # TO-DO
    arr_a_index=0
    arr_b_index=0
    for i in range(0, len(merged_arr)):
        if arr_a_index == len(arrA):
            merged_arr[i]=arrB[arr_b_index]
            arr_b_index+=1 
        elif arr_b_index==len(arrB):
            merged_arr[i]=arrA[arr_a_index]
            arr_a_index+=1 
        elif arrA[arr_a_index] < arrB[arr_b_index]:
            merged_arr[i]=arrA[arr_a_index]
            arr_a_index+=1        
        elif arrA[arr_a_index] > arrB[arr_b_index]:
            merged_arr[i]=arrB[arr_b_index]
            arr_b_index+=1    
           
       
    return merged_arr

# arrayA = [4,2,1,5,8]
# arrayB = [3,6,9,7,10]
# merge(arrayA, arrayB)

# print(merge(arrayA, arrayB))
# TO-DO: implement the Merge Sort function below USING RECURSION

def merge_sort( arr ):
    # TO-DO
    # Divide the arr in half
    # base case
    if len(arr) < 2:
        return arr
    else:
        A = arr[:len(arr)//2]
        B = arr[len(arr)//2:]
        return merge(merge_sort(A), merge_sort(B))
        
    
    
    # if len(A) == 1:
    #     return A
    # elif len(B) == 1:
    #     return B
    # else:
    #     merge_sort(A)
    #     merge_sort(B)
      
    
    
      
    # Recursively divide the array
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
