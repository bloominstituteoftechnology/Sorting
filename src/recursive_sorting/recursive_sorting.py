# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    merged_arr = []

    #While arrA is not empty and arrB is not empty 
    while len(arrA) >= 1 and len(arrB) >= 1:
        if arrA[0] <= arrB[0]:
            merged_arr.append(arrA[0])
            arrA = arrA[1:] 
        else:
            merged_arr.append(arrB[0])
            arrB = arrB[1:]
    
    while len(arrA) >=1:
        merged_arr.append(arrA[0])
        arrA = arrA[1:] 
    
    while len(arrB) >=1:
        merged_arr.append(arrB[0])
        arrB = arrB[1:]
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # Base Case if array is empty or length 1
    if len(arr) <= 1:
        return arr
    # Split arrays into half
    arrA = []
    arrB = []
    for i , x in enumerate(arr):
        if i < len(arr)/2:
            arrA.append(x)
        else:
            arrB.append(x)
    # Sort each half
    arrA = merge_sort(arrA)
    arrB = merge_sort(arrB)
    # Merge back together
    return merge(arrA, arrB)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Maintain two pointers which point to start of the segments which have to be merged.
    start2 = mid + 1
    # Compare the elements at which the pointers are present.
    if arr[mid] <= arr[start2]:
        return
    
    while start <= mid and start2 <= end:
        # If element1 < element2 then element1 is at right position, simply increase pointer1.
        if arr[start] <= arr[start2]:
            start += 1
        # Else place element2 in its right position and all the elements at the right of element2 will be shifted right by one position. 
        else:
            val = arr[start2]
            i = start2

            while i != start:
                arr[i] = arr[i - 1]
                i -= 1
            
            arr[start] = val

            # Increment all the pointers by 1.
            start += 1
            mid += 1
            start2 += 1

def merge_sort_in_place(arr, l, r): 
    
    if l < r:
        
        m = (l + (r - 1)) // 2
        
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)
        
        merge_in_place(arr, l, m, r)
    
    return arr

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
