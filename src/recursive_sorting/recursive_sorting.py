# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    merged_arr = []
    i_of_a, i_of_b = 0, 0
    # TO-DO
    while i_of_a < len(arrA) and i_of_b < len(arrB):
        if arrA[i_of_a] < arrB[i_of_b]:
            merged_arr.append(arrA[i_of_a])
            i_of_a+=1
        else:
            merged_arr.append(arrB[i_of_b])
            i_of_b+=1
    if i_of_a == len(arrA): merged_arr.extend(arrB[i_of_b:])
    else:                   merged_arr.extend(arrA[i_of_a:])
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1: return arr
    if len(arr) == 2: merge([arr[0]],[arr[1]])
    L, R = merge_sort(arr[ : len(arr) // 2]), merge_sort(arr[ len(arr) // 2 : ])
    return merge(L,R)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    L, R, i_of_L, i_of_R = arr[start:mid] ,arr[mid:end], 0, 0
    for k in range(start,end):
        if i_of_R >= len(R) or (i_of_L < len(L) and L[i_of_L] < R[i_of_R]):
            arr[k] = L[i_of_L]
            i_of_L += 1
        else:
            arr[k] = R[i_of_R]
            i_of_R += 1 
    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO
    if r - l > 1:
        mid = int((l+r)/2)
        merge_sort_in_place(arr,l,mid)
        merge_sort_in_place(arr,mid,r)
        merge_in_place(arr,l,mid,r)
    return arr

A  = [20, 30, 21, 15, 42, 45, 31, 0, 9]
merge_sort_in_place(A,0,len(A))
print(A)

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
