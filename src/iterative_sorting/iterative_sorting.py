arr = [3,22,17,1,20,8,31,137, 12, 4, 19, 20, 2, 9]
# arr = [7, 12, 4, 19, 20, 2, 9]
# arr = [3,22,17,1,20,8,31,13]
print(arr,"Begin selection \n")

# TO-DO: Complete the selection_sort() function below


def selection_sort( arr ):
	length = len(arr)
	breakcount =0
	# loop through n-1 elements
	for i in range(0, len(arr) - 2):
		breakcount+=1
		
		cur_index = i
		smallest_index = cur_index

		for j in range( i + 1, length ):
			if arr[j] < arr[smallest_index]:
				smallest_index = j
		
		if smallest_index != i:
			move = arr.pop(smallest_index)
			arr.insert(i, move)
		
		if breakcount > 20:
			print(20, 20)
			break

		print(29,arr)

	return arr

print(35,selection_sort(arr),"selection\n\n") 






# TO-DO:  implement the Bubble Sort function below

arr = [3,22,17,1,20,8,31,137, 12, 4, 19, 20, 2, 9]
# arr = [7, 12, 4, 19, 20, 2, 9]
# arr = [3,22,17,1,20,8,31,13]

print(arr,"Begin bubble\n")

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

		if breakcount > 20:
			print(20, 20)
			break

		print(65,arr)
		
	return arr

print(77,bubble_sort(arr),"bubble") 


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

	return arr