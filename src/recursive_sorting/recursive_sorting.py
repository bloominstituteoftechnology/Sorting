# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        middle = len(arr) // 2
        tail = arr[:middle]
        head = arr[middle:]

        merge_sort(head)
        merge_sort(tail)

        a = b = c = 0
        
        while a < len(head) and b < len(tail):
            if head[a] < tail[b]:
                arr[c] = head[a]
                a += 1
            else:
                arr[c] = tail[b]
                b += 1
            c += 1

        while a < len(head):
            arr[c] = head[a]
            a += 1
            c += 1

        while b < len(tail):
            arr[c] = tail[b]
            b += 1
            c += 1
    return arr


# STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO
#
#     return arr
#
# def merge_sort_in_place(arr, l, r):
#     # TO-DO
#
#     return arr
#
#
# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort( arr ):
#
#     return arr
