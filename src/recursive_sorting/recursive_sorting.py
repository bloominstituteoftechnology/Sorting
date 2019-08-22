# TO-DO: complete the helpe function below to merge 2 sorted arrays


def merge(arrA, arrB):
    merged_arr = []
    while True:
        if arrA and arrB:
            if arrB[0] < arrA[0]:
                merged_arr.append(arrB.pop(0))
            else:
                merged_arr.append(arrA.pop(0))
        else:
            merged_arr += arrA
            merged_arr += arrB
            break
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # split list
    if len(arr) > 1:
        l = arr[:len(arr)//2]
        r = arr[len(arr)//2:]
        return merge(merge_sort(l), merge_sort(r))
    else:
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
def timsort(arr):

    return arr
