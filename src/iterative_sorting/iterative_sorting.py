# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
  # loop through n-1 elements
  for i in range(0, len(arr) - 1):
      cur_index = i
      smallest_index = cur_index
      smallest_value = arr[cur_index]
      cur_value = arr[cur_index]
      
      # TO-DO: find next smallest element
      # (hint, can do in 3 loc) 

      for j in range(i + 1, len(arr)):

        while smallest_value > arr[j]:
          smallest_index = j
          smallest_value = arr[j]
          
      # TO-DO: swap
      arr[cur_index] = smallest_value
      arr[smallest_index] = cur_value
        
  return arr

selectArray = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

# selection_sort(selectArray)

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
  temp = 0

  for i in range(0, len(arr) - 1):
    for j in range(0, len(arr) - 1):
      if arr[j] > arr[j + 1]:
        temp = arr[j]

        arr[j] = arr[j + 1]

        arr[j + 1] = temp
                 
  return arr

bubbleArray = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

bubble_sort(bubbleArray)

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr