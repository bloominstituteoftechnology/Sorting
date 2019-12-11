# TO-DO: complete the helper function below to merge 2 sorted arrays

# Ex 1


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    merged_arr = arrA + arrB
    print(merged_arr)

    return merged_arr


# merge([2, 2, 3], [2, 2, 3])


# # TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    #     # TO-DO
    if len(arr) > 1:
        middle = len(arr) // 2
        left_half = arr[:middle]
        right_half = arr[middle:]
        print("1. Left: ", left_half)
        print("1. Right: ", right_half)
        print("Array: ", arr, "\n")

        # Recursive call on each half to divide them
        merge_sort(left_half)
        merge_sort(right_half)

        # iterator to traverse left_half
        i = 0
        # iterator traverse right_half
        j = 0
        # Iterator of main
        k = 0

        while i < len(left_half) and j < len(right_half):
            print(left_half)
            print(right_half)
            print("\nMain While")
            print("Array: ", arr)
            print("left_half[i]: ", left_half[i])
            print("right_half[j]: ", right_half[j], "\n")
            if left_half[i] < right_half[j]:
                print(f'{left_half[i]} < {right_half[j]}')
                print("MW IfLeft left_half[i] :", left_half[i])
                arr[k] = left_half[i]
                print("MW IfLeft arr[k]: ", arr[k])
                print("MW IfLeft arr: ", arr, "\n")

                i += 1
            else:
                print(f'{left_half[i]} > {right_half[j]}')
                print("MW IfRight right_half[j] :", right_half[j])
                arr[k] = right_half[j]
                print("MW IfRight arr[k]: ", arr[k])
                print("MW IfRight arr: ", arr, "\n")
                j += 1

            k += 1

        # For remaining values
        while i < len(left_half):
            print("While Left.")
            print("WL left_half[i]: ", left_half[i])
            arr[k] = left_half[i]
            print("WL : ", arr)
            i += 1
            k += 1

        while j < len(right_half):
            print("While Right")
            print("WR right_half[j]: ", right_half[j])
            arr[k] = right_half[j]
            print("WR : ", arr)
            j += 1
            k += 1

    return arr


print(merge_sort([3, 7, 1, 5, 11, 4, 2]))


# Ex 2

# def merge(leftArray, rightArray):
#     # merged_arr = [0] * elements
#     merged_arr = []

#     i, j = 0, 0

#     while i < len(leftArray) and j < len(rightArray):
#         if leftArray[i] <= rightArray[j]:
#             merged_arr.append(leftArray[i])
#             i += 1
#         else:
#             merged_arr.append(rightArray[j])
#             j += 1

#     merged_arr += leftArray[i:]
#     merged_arr += rightArray[j:]

#     return merged_arr


# def merge_sort(arr):
#     if len(arr) < 2:
#         return arr
#     middle = len(arr) // 2
#     left_half = arr[:middle]
#     right_half = arr[middle:]

#     left_half_merge_sort = merge_sort(left_half)
#     right_half_merge_sort = merge_sort(right_half)

#     return merge(left_half_merge_sort, right_half_merge_sort)


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
