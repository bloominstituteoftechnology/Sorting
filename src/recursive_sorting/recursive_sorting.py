# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    result = []
    i = j = 0
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            result.append(arrA[i])
            i+=1
        else:
            result.append(arrB[j])
            j+=1
    result += arrA[i:]
    result += arrB[j:]


    return result


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) < 2:
        return arr
    mid = len(arr)//2

    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])

    return merge(left,right)



# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
def timsort( arr ):

    return arr
