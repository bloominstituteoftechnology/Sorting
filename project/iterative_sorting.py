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
      if arr[j] < [smallest_index]: 
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


# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):

    return arr


# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr