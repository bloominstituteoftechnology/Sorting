# TO-DO: complete the helpe function below to merge 2 sorted arrays

"""need to compare the numbers and sort the elements one by one start with left first index and compare to first right index, if left is smaller put into array and them compare second element to right first and if right is small push to new array and then compare left second element to second right element."""


def merge(arrA, arrB):

    merged_arr = []

    # TODO
    i = 0
    j = 0
    while (i < len(arrA) and j < len(arrB)):
        print(f"i: {i}")
        print(f"j: {j}")
            merged_arr.append(arrA[i])
            i += 1
        else:
            merged_arr.append(arrB[j])
            j += 1
    while (i < len(arrA)):
        merged_arr.append(arrA[i])
        i += 1
    while (j < len(arrB)):
        merged_arr.append(arrB[j])

    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    middle = len(arr) // 2

    arrA = arr[:middle]
    arrB = arr[middle:]

    merge_sort(merge(arrA, arrB))
    return arr


merge_sort([23, 45, 21, 65, 78])
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
