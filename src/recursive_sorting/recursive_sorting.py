# TO-DO: complete the helper function below to merge 2 sorted arrays



'''
Both arrA and arrB are already sorted, so only need to compare
the same index of each to each other and store the value
that is smaller in the merged_arr.  Starting at index 0 for 
both arrays, the while loop runs as long as the length of the 
arrays are valid
'''
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
   
    # TO-DO
    a = 0
    b = 0
    

    for i in range (0, elements):
        if a>= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a =+ 1
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a +=1
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a +=1
        else:
            merged_arr[i] = arrB[b]
            b += 1


    return merged_arr



'''
Pseudo code for merge sort in place
1. maintain two pointers that point to both halves that need to be sorted
2. compare the elements for where the pointers are present
3. if element1 < element2, then element1 is in the right place, so increase the pointer to the next item
4. Else place element2 in its right position and all the elements at the right of element2 will be shifted right by one position. Increment all the pointers by 1.
'''

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    n = len(arr)
    if n < 2: 
        return arr

    mid = n //2 #divide number by integer of 2 to get mid
    arr_l = arr[:mid]
    arr_r = arr[mid:]

    return merge(merge_sort(arr_l), merge_sort(arr_r))
   


