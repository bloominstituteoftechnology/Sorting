# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
  # loop through n-1 elements
  for i in range(0, len(arr) - 1):
    cur_index = i
    smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
    for j in range(i+1,len(arr)):
      if arr[j] < arr[i]:
        smallest_index = j
    element = arr[cur_index]
    arr[i] = arr[smallest_index]
    arr[smallest_index] = element

        # TO-DO: swap




    return arr


# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):
  for n in range(1,len(arr)):
    element = arr[n]
    while n > 0 and n[-1] < element:
      arr[n] = arr[n-1]
        n = n-1
        arr[n] = element
  return arr


# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr