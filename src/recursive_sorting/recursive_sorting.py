# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)

    # merged_arr = [0] * elements
    merged_arr = []
    # TO-DO

    # For the lenth of the one array, insert the smallest element from both arrays in front
    # first attempts

    # for i in range(len(merged_arr)):

    #     smallest = arrA[0]
    #     if len(arrA) > 0:
    #         for e in range(len(arrA)-1):
    #             print('a', arrA[e])
    #             print(smallest)
    #             if smallest >= arrA[e]:
    #                 print(smallest, arrA[e])
    #                 smallest = arrA[e]
    #                 arrA.remove(arrA[e])
    #     if len(arrB) > 0:
    #         for e in range(len(arrB)-1):
    #             if smallest >= arrB[e]:
    #                 smallest = arrB[e]
    #                 arrB.remove(arrB[e])
    #     result_arr.append(smallest)
    # print(arrA[e])
    # if not e == len(arrB):
    #     print(arrB[e])
    #     merged_arr.append(arrA[e])

    # if arrA[e] < arrB[e]:
    #     merged_arr.append(arrA[e])
    #     merged_arr.append(arrB[e])
    # else:
    #     merged_arr.append(arrB[e])
    #     merged_arr.append(arrA[e])

    # =================================
    # While current left index is less then left length and right index is less then right length
    # If left element is bigger then right element
    # add left element to result and move to next left index
    # else add right element to result and move to next right index

    aIndex = 0
    bIndex = 0

    while aIndex < len(arrA) and bIndex < len(arrB):
        if arrA[aIndex] < arrB[bIndex]:
            merged_arr.append(arrA[aIndex])
            aIndex += 1
        else:
            merged_arr.append(arrB[bIndex])
            bIndex += 1

    # put any remaining indicies on the end of the array
    print('b', arrA[aIndex:], arrB[bIndex:])
    for e in arrA[aIndex:]:
        merged_arr.append(e)
    for e in arrB[bIndex:]:
        merged_arr.append(e)

    # for i in range(len(merged_arr)):
    # print('wow', merged_arr)
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO

    middle = len(arr)//2
    # print(middle
    if len(arr) > 1:
        # left = (arr[:middle])
        # right = (arr[middle:])
        # print(right, left)
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        return merge(right, left)

    return arr


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# merge([1, 2, 3, 7], [4, 5, 6])
print(merge_sort([2, 1, 3, 5]))

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
