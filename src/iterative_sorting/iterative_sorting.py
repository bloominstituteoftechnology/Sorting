# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
	# loop through n-1 elements
	for i in range(0, len(arr) - 1):
		cur_index = i
		smallest_index = cur_index
		# TO-DO: find next smallest element
		# (hint, can do in 3 loc) 
			 



		# TO-DO: swap




	return arr


# TO-DO:  implement the Bubble Sort function below

arr = [7, 12, 4, 19, 20, 2, 9]
print(24,arr,"Begin\n")


def bubble_sort( arr ):

	working = True
	breakcount = 0

	for i in range(len(arr)-1):
		breakcount+=1
		count = 0
		working = False
		
		for j in range(len(arr)-1):
			cur = arr[j]
			nex = arr[j+1]

			if cur > nex:
				move = arr.pop(j+1)
				arr.insert(j, move)
				working = True

		if not working:
			break

		if breakcount > 10:
			print(10, 10)
			break

		print(65,arr)
		
	return arr


print("\nbubble", bubble_sort(arr)) 


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

	return arr