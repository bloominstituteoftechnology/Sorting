# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
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

print(selection_sort([45,23,46,1,4,5]))


# # TO-DO: implement the Insertion Sort function below
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
print(insertion_sort([45,23,46,1,4,5]))


# # STRETCH: implement the Bubble Sort function below
# def bubble_sort( arr ):

#     return arr


# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr