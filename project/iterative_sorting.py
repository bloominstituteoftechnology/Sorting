# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
  # loop through n-1 elements
  for i in range(0, len(arr) - 1):
    cur_index = i
    smallest_index = cur_index
    for j in range(i+1,len(arr)):
      if arr[j] < arr[smallest_index]:
        smallest_index = j
    arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

        # TO-DO: swap
  return arr


# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):
  for n in range(1,len(arr)):
    element = arr[n]
    while n > 0 and arr[n-1] > arr[n]:
      arr[n], arr[n-1] = arr[n-1], arr[n]
      n = n-1    
  return arr


# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):
    for n in range(0,len(arr)-1):
      if arr[n] > arr[n+1]:
        unsorted = True
        arr[n], arr[n+1] = arr[n+1], arr[n]
      if n == len(arr-1) and unsorted:
        unsorted = False
        n = 0
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
 pass

