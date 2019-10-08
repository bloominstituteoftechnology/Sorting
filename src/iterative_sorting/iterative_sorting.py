# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i

        while j > 0 and temp < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1

        arr[j] = temp
    return arr

# TO-DO:  implement the Bubble Sort function below

# Used this website to understand Bubble Sort: http://www.pkirs.utep.edu/CIS3355/Tutorials/chapter9/tutorial9A/bubblesort.htm
# Warning: God awful design. Also step 2 should be: Compare second and third elements '7' and '2'.
       #Grab the current index of array and compare it to the index to the right
       #If the index to the right is larger than the index to the left, swap positions.
       #Else compare the next two indexes.

def bubble_sort( arr ):
  for i in range(0, len(arr) - 1):
    plusOne = arr[i + 1]
    plusNone = arr[i]
    if arr[i] > arr[i + 1]:
      arr[i] = plusOne
      arr[i + 1] = plusNone
      bubble_sort(arr)
  print(arr)
  return arr
# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr