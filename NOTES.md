# selection_sort
  Traverse entire array and find smallest value
  Swap current value for the smallest

# insertion_sort
  start at the beginning of the array
  compare first value to second value and swap if needed

# bubble_sort
  Traverse the entire array and sort consecutive items.
  Traverse the entire array again repeatedly until the array is in order

# count_sort
  Create frequency array for all numbers where: 
    the index is the value of the original array and 
    the value is the frequency
    add the previous value to the current value
  Create an array the length of the original array
    take the first value in the original array
    find it's counterpart index in the freq array
    place that first value in the original array at the index of the freq

  For simplicity, only use data in the range of 0 - 9. 
  So the frequency array would have a length of 10.
  https://www.youtube.com/watch?v=7zuGmKfUt7s

# quick


# Choosing a sorting method
  Quicksort (divide and conquer) is better when the sub problems are independent of each other.
  Dynamic programming for dependent sub problems (Fibonnaci)
    combination problems will generally have dependent sub-problems