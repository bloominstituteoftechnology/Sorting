# TO-DO: complete the helper function below to merge 2 sorted arrays

arrA = [1, 2, 3, 4, 5]
arrB = [6, 7, 8, 9, 10]

print('\n~~~ merge function starts ~~~~')
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    merged_arr = arrA + arrB
    # TO-DO

    print("arrA ~~~>", arrA)
    print("arrB ~~~>", arrB)
    print("merged_arr ~~~>", merged_arr, '\n~~~ merge function ends ~~~\n')

    return merged_arr

merge(arrA, arrB)




'''
plan
base case:  if array length 0 or 1
 return array
else:
pick pivot might as well pick first because its unsorted, none are better
put anything smaller into left array
put anything bigger into right array
return quicksort(left) + quicksort(right)
'''


# TO-DO: implement the Merge Sort function below USING RECURSION
arr = [5,4,6,7,9,1,2,3]
def merge_sort(arr):
    set_a= [0, len(arr) //2 ]
    set_b= [len(arr ) // 2 + 1, arr[-1]]
    if len(arr) == 1:
        return arr

    for i in arr:
        print("arr in range_a = ~~~>",arr[range_a])
    '\n'

    print("range_a = ~~~>", set_a)
    print("range_b = ~~~>", set_b)
    return arr

merge_sort(arr)
print("baseCase or modified arr ~~~>",arr, '\n')









# # STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO
#     return arr
# def merge_sort_in_place(arr, l, r):
#     # TO-DO
# return arr

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort(arr):
#     return arr
