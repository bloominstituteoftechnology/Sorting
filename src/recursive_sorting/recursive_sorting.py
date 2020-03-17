#!/usr/bin/env python


# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(a, b):
	merged = []
	while a and b:
		if a[0] < b[0]:
			merged.append(a.pop(0))
		else:
			merged.append(b.pop(0))
	merged.extend(a if a else b)

	return merged


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(array):
	if len(array) > 1:
		divide_index = len(array) // 2
		array = merge(
			merge_sort(array[:divide_index]),
			merge_sort(array[divide_index:])
		)

	return array


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
	# TO-DO

	return array

def merge_sort_in_place(arr, l, r):
	# TO-DO

	return array


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(array):

	return array


array = [8, 5, 2, 1, 3, 4, 3, 9, 7, 0, 4, 10, 9]
print(merge_sort(array[:]))


