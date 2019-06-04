import time
import random
from bisect import bisect, insort_right

def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    mi = 0
    while len(arrA) or len(arrB):
        while len(arrA) > 0 and len(arrB) > 0:
            if arrA[0] <= arrB[0]:
                merged_arr[mi] = arrA[0]
                mi += 1
                arrA = arrA[1:]
            else:
                break

        while len(arrB) > 0 and len(arrA) > 0:
            if arrB[0] <= arrA[0]:
                merged_arr[mi] = arrB[0]
                mi += 1
                arrB = arrB[1:]
            else:
                break
        if len(arrA) == 0 and len(arrB) > 0:
            for i in range(mi, len(merged_arr)):
                merged_arr[i] = arrB[0]
                arrB = arrB[1:]
        elif len(arrA) > 0 and len(arrB) == 0:
            for i in range(mi, len(merged_arr)):
                merged_arr[i] = arrA[0]
                arrA = arrA[1:]

    return merged_arr


arrA = [1, 15, 8, 10]
arrB = [11, 16, 21, 26]
# print(merge(arrA, arrB))


def merge_quick_sort(arr, merge_sort=True):
    L = len(arr)
    if L <= 1:
        return arr
    # if len(arr) == 2:
    #     if arr[0] > arr[1]:
    #         return [arr[1],arr[0]]
    #     return arr

    # if len(arr) >= 2:
    assert L >= 2, f'logic error arr len {len(arr)}'
    if merge_sort:
        n = L // 2
        return merge(merge_quick_sort(arr[0:n]), merge_quick_sort(arr[n:]))
    else:
        p = arr[0]
        arr = arr[1:]
        L = len(arr)
        arrl = []
        arrh = []
        dc = 1
        for i in range(0, L):
            if arr[i] < p:
                arrl.append(arr[i])
            elif arr[i] > p:
                arrh.append(arr[i])
            else:  # equal
                dc += 1
        p = [p] * dc
        # print('checklength', L, dc + len(arrl) + len(arrh))
        # print('p', p, type(p))
        arr = merge_quick_sort(arrl, False)
        arr.extend(p)
        # print('type arr', type(arr))
        arr.extend(merge_quick_sort(arrh))
        return arr

def quick_sort_A( books, low, high ):  # class in-place merge sort
    # base case
    if low >= high:
        return books
    # recursive case
    else:
        # divide
        pivot_index = low
        # for each element in subarray
        for i in range(low, high):
            if books[i] < books[pivot_index]:
                # double swap to move smaller elements to correct index
                # move current element to the right of pivot
                temp = books[pivot_index+1]
                books[pivot_index+1] = books[i]
                books[i] = temp

                # swap pivot with element on its right
                temp = books[pivot_index]
                books[pivot_index] = books[pivot_index+1]
                books[pivot_index+1] = temp
                pivot_index += 1

        # conquer
        # Quick Sort everything left of the pivot
        books = quick_sort_A(books, low, pivot_index)
        # Quick Sort everything right of the pivot
        books = quick_sort_A(books, pivot_index+1, high)
  
        return books

arrB.extend(arrA)
arr = random.sample(range(200000), 50000)
print('initial arr len', len(arr))
clk_id = time.CLOCK_PROCESS_CPUTIME_ID
start = time.clock_gettime_ns(clk_id)
merge_quick_sort(arr, False)
print('my quick time\t\t\t',(time.clock_gettime_ns(clk_id) - start) / 1e9 )
# start = time.clock_gettime_ns(clk_id)
# merge_quick_sort(arr, True)
# print('merge sort time\t\t\t',(time.clock_gettime_ns(clk_id) - start) / 1e9 )
start = time.clock_gettime_ns(clk_id)
quick_sort_A(arr, 0, len(arr))
print('class merge in-place sort time\t',(time.clock_gettime_ns(clk_id) - start) / 1e9 )


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

#  timsort uses an equivalent to Python's bisect.bisect_right
#  bisect.insort_right is equivalent to list.insert(bisect.bisect_right(list, item, lo, hi), item).
def insort_right_sort(arr):
    r = [arr[0]]
    for i in arr[1:]:
        insort_right(r,i)
    return r

# print('insort_right', insort_right_sort([3,2,4,1]))
start = time.clock_gettime_ns(clk_id)
insort_right_sort(arr)
print('insort_right_sort time\t\t',(time.clock_gettime_ns(clk_id) - start) / 1e9 )

def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
