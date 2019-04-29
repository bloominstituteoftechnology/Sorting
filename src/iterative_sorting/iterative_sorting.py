def insertion_sort(arr):
	for i in range(1, len(arr)):
		temp = arr[i]
		j = i
		while j > 0 and temp < arr[j-1]:
			arr[j] = arr[j-1]
			j -= 1
		arr[j] = temp
	return arr


print(insertion_sort([ 1,3,6,2,13,41,7 ]))

# TO-DO: Complete the selection_sort() function below 
def selection_sort(l):
	list_length = len(l)
	# loop through n-1 elements
	for i in range(0, list_length-1):
		cur_index = i
		smallest_index = cur_index
		# TO-DO: find next smallest element
		# (hint, can do in 3 loc); what's loc?
		while cur_index < list_length:
			if l[cur_index] < l[smallest_index]:
				# TO-DO: swap
				l[smallest_index], l[cur_index] = l[cur_index], l[smallest_index]
			cur_index += 1
	return l


print(selection_sort([ 1,3,6,2,13,41,7 ]))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
	return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum = -1):
	return arr
