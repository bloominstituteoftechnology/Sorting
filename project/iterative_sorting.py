# Complete the selection_sort() function below in class with your instructor
# selection sort is sort in place
def selection_sort(arr):
  # loop through n-1 elements
  for i in range(0, len(arr) - 1):
    cur_index = i
    smallest_index = cur_index
    # TO-DO: find next smallest element
    # (hint, can do in 3 loc) 
    for j in range(cur_index, len(arr)):
      if arr[j] < arr[smallest_index]: 
        #if j is less than smallest then make j the new smallest
          smallest_index = j
    # TO-DO: swap
    # swap the next element with the next smallest every time till it's sorted
    temp = arr[smallest_index]
    arr[smallest_index] = arr[cur_index]
    arr[cur_index] = temp
  return arr
 # O(n^2)
my_arr = [2,5,9,7,4,1,3,8,6]
print(selection_sort(my_arr))
print(f'This is selection sort {selection_sort(my_arr)}')


# TO-DO: implement the Insertion Sort function below
# first element is sorted sub array of the array
# pull items from unsorted array and put them in the right place in the array
# sorted in place
def insertion_sort(arr):
  for i in range(1, len(arr)):
    # do sorting from index 1 to the rest of the list b/c first one is sorted subarray
    current_item = arr[i]
    j = i-1 # previous number from current
    while j >=0 and current_item < arr[j]: 
      arr[j+1] = arr[j] 
      j -= 1
      arr[j+1] = current_item 
  return arr
print(f'This is insertion sort {insertion_sort(my_arr)}')

# STRETCH: implement the Bubble Sort function below
def bubble_sort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      # last item will be in place
      # Swap if item is greater
      if arr[j] > arr[j+1]:
          arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr

print(f'This is bubble sort {bubble_sort(my_arr)}')

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr