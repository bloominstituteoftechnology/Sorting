from random import randint
def quick_sort(arr):
  pivot = randint(0, len(arr) - 1)
  left = []
  right = []
  for num in arr[:pivot] + arr[pivot+1:]:
    if num < arr[pivot]:
      left.append(num)
    else:
      right.append(num)
  if len(left) > 1:
    left = quick_sort(left)
  if len(right) > 1:
    right = quick_sort(right)
  return left + [arr[pivot]] + right


print(quick_sort([1, 3, 6, 2, 13, 41, 7]))

# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO

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
