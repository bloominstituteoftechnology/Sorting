# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    a = 0
    b = 0
    for i in range(0, elements):
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        elif b > len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] > arrB[b]:
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        merge_sort(L) # Sorting the first half 
        merge_sort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1   
    return arr
         
    # TO-DO
      

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    L = arr[start:mid]
    R = arr[mid:end]
    i = 0
    j = 0
    k = start
    for l in range(k,end):
        if j >= len(R) or (i < len(L) and L[i] < R[j]):
            arr[l] = L[i]
            i = i + 1
        else:
            arr[l] = R[j]
            j = j + 1  
    return arr

    def merge_sort_in_place(arr, l, r): 
    # TO-DO
        if r - p > 1:
            mid = int((l+r)/2)
            mergeSort(arr,l,mid)
            mergeSort(arr,mid,r)
            merge_in_place(arr,l,mid,r)
        return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
