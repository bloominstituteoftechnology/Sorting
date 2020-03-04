# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    merged_arr = []
    # TO-DO
    left = 0
    right = 0
    # piv = 0

    while left < len(arrA) and right < len(arrB):
        if arrA[left] <= arrB[right]:
            merged_arr.append(arrA[left])
            left += 1
        else:
            merged_arr.append(arrB[right])
            right += 1
    return merged_arr + arrA[left:] + arrB[right:]

    # while left < len(arrA) and right < len(arrB):
    #     if arrA[left] < arrB[right]:
    #         merged_arr.append(arrA[left])
    #         left += 1
    #     else:
    #         merged_arr.append(arrB[right])
    #         right += 1
    #     if left >= len(arrA):
    #         merged_arr += arrB[right:]
    #     elif right >= len(arrB):
    #         merged_arr += arrA[left:]

    # return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr

    # if len(arr) == 2:
    #     base_case = [[num] for num in arr]
    #     return merge(base_case[0], base_case[1])

    pivot = len(arr) // 2
    left = merge_sort(arr[0:pivot])
    right = merge_sort(arr[pivot:])
    # return merge(merge_sort(arr[:pivot]), merge_sort(arr[pivot:]))
    # return arr
    return merge(left, right)

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
