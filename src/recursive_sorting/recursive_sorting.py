# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = []
    i,j = 0,0
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr.append(arrA[i])
            i += 1
        else:
            merged_arr.append(arrB[j])
            j += 1
    
    # This last bit gets us the odd item out that would otherwise trip error
    merged_arr = merged_arr + arrA[i:] + arrB[j:]
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:

        middle = len(arr)//2
        left = arr[:middle]
        right = arr[middle:]
        
        merge_sort(left)
        merge_sort(right)
        
        i = j = k = 0
        
        # Copy data to temp arrays L[] and R[] 
        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                arr[k] = left[i] 
                i+=1
            else: 
                arr[k] = right[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(left): 
            arr[k] = left[i] 
            i+=1
            k+=1
          
        while j < len(right): 
            arr[k] = right[j] 
            j+=1
            k+=1
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
