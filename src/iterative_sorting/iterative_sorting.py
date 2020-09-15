#!/usr/bin/env python


def min_from_index(array, start_index):
	min_value = array[start_index]
	min_index = start_index
	for i in range(start_index + 1, len(array)):
		if array[i] < min_value:
			min_value = array[i]
			min_index = i
	return (min_index, min_value)


def selection_sort(array):
	for i in range(0, len(array) - 1):
		smallest_index, _ = min_from_index(array, i)
		smallest = array.pop(smallest_index)
		array.insert(i, smallest)
	return array


def bubble_sort(array):
	done = False
	while not done:
		done = True
		for index in range(len(array) - 1):
			cur_value = array[index]
			next_value = array[index + 1]
			if cur_value > next_value:
				array.pop(index + 1)
				array.insert(index, next_value)
				done = False
	return array


def optimized_bubble_sort(array):
	# This is basically just Gnome Sort, approaching insertion sort
	# Leaving it in here for posterity
	index = 1
	greatest = index
	while index < len(array) - 1:
		print(array[:index] + [[array[index]]] + array[index + 1:])
		# print((index, array[index]))
		if index == 0:
			# If we're at the start of the array, increment
			index += 1
		prev_value = array[index - 1]
		cur_value = array[index]
		next_value = array[index + 1]
		if cur_value > next_value:
			# Swap with the next value and wiat
			array.pop(index + 1)
			array.insert(index, next_value)
		elif cur_value < prev_value:
			# Swap with the previous value and decrement
			array.pop(index)
			array.insert(index - 1, cur_value)
			index -= 1
		elif index < greatest:
			# Jump to the index after where we left off
			index = greatest + 1
		else:
			# Increment
			index += 1
			greatest = index
	return array


def count_sort(array, maximum=-1):
	if len(array) == 0:
		return array
	if min(array) < 0:
		raise ValueError
	counts = [0 for _ in range(max(array) + 1)]
	for value in array:
		counts[value] += 1
	for index in range(1, len(counts)):
		counts[index] += counts[index - 1]
	new_array = array[:]
	for value in array:
		counts[value] -= 1
		index = counts[value]
		new_array[index] = value
	return new_array


array = [8, 5, 2, 1, 3, 4, 3, 9, 7, 0, 4, 10, 9]

print(selection_sort(array[:]))

print(bubble_sort(array[:]))

print(optimized_bubble_sort(array[:]))

print(count_sort(array[:]))

