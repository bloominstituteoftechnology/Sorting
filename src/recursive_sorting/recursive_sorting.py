# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []

    while len(arrA) > 0 or len(arrB) > 0:
        if len(arrA) == 0 and len(arrB) > 0:
            merged_arr += arrB
            break
        elif len(arrA) > 0 and len(arrB) == 0:
            merged_arr += arrA
            break
        else:
            if arrA[0] <= arrB[0]:
                merged_arr.append(arrA.pop(0))
            else:
                merged_arr.append(arrB.pop(0))

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr

    left = merge_sort(arr[:len(arr)//2])
    right = merge_sort(arr[len(arr)//2:])

    return merge(left, right)


# STRETCH: implement an in-place merge sort algorithm
# Reference: https://www.geeksforgeeks.org/in-place-merge-sort/
def merge_in_place(arr, start, mid, end):
    # TO-DO
    """
    1. Maintain two pointers which point to start of the segments which
    have to be merged.
    2. Compare the elements at which the pointers are present.
    3. If element1 < element2 then element1 is at right position,
    simply increase pointer1.
    4. Else place element2 in its right position and all the elements
    at the right of element2 will be shifted right by one position.
    Increment all the pointers by 1.
    """
    start2 = mid+1

    # if arr[mid] <= arr[start2]:
    #     return

    while start <= mid and start2 <= end:
        if arr[start] <= arr[start2]:
            # Element in right place do nothing
            start += 1
        else:
            value = arr[start2]
            index = start2

            # Shift all the elements between element 1
            # element 2, right by 1.
            while index >= start:
                arr[index] = arr[index-1]
                index -= 1

            # Copy the value at start
            arr[start] = value

            start += 1
            mid += 1
            start2 += 1

    return


def merge_sort_in_place(arr, l, r):
    # TO-DO
    # Split the array into 2
    if l < r:
        m = (l + r) // 2

        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m+1, r)

        merge_in_place(arr, l, m, r)

    return arr


# STRETCH: implement the Timsort function below
# hint:
# check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
