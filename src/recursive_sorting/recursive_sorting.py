# Helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    merged_arr = []
    i_of_a, i_of_b = 0, 0
    # We initiate a loop to continue to iterate until 1 of the 2 arrays we recieved as inputs has been completed. We will then tack
    # Whatever is left of the remaining array to the end of our Merged array, as it already sorted at this point. 
    while i_of_a < len(arrA) and i_of_b < len(arrB):
        # Next we will need to compare the individual values within each of our 2 input arrays, compare, and append the lesser value
        # TO the end of the sorted Return array.
        if arrA[i_of_a] < arrB[i_of_b]:
            merged_arr.append(arrA[i_of_a])
            i_of_a+=1
        else:
            merged_arr.append(arrB[i_of_b])
            i_of_b+=1
    # Tack on the last remnant of which ever array be it A or B to the end of our newly sorted list
    if i_of_a == len(arrA): merged_arr.extend(arrB[i_of_b:])
    else:                   merged_arr.extend(arrA[i_of_a:])
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # First we will acount for the Base/edge case of to handle the last case of recurssion recieving a bad input or one of an array with a 
    # singular value stored within it.
    if len(arr) <= 1: return arr
    # Here we take our input array and split it in to 2 segments, one from the start to the middle, the other from the middle to the end
    # using a call stack(allowing the machine to keep tracking of the ever changing data using recursion) initialized by recursively calling
    # Our function.
    L, R = merge_sort(arr[ : len(arr) // 2]), merge_sort(arr[ len(arr) // 2 : ])
    # Now that both our left and our right arrays are both sorted, we can sort both the left and right arrays into eachother now.
    return merge(L,R)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    l, r, i_of_l, i_of_r = arr[start:mid], arr[mid:end], 0, 0
    for k in range(start, end):
        if i_of_r >=len(r) or (i_of_l < len(l) and l[i_of_l] < r[i_of_r]):
            arr[k] = l[i_of_l]
            i_of_l += 1
        else:
            arr[k] = r[i_of_r]
            i_of_r += 1
    return arr

def merge_sort_in_place(arr, l, r): 
    if r - l > 1:
        mid = int((l+r)/2)
        merge_sort_in_place(arr, l, mid)
        merge_sort_in_place(arr, mid, r)
        merge_in_place(arr, l, mid, r)
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
