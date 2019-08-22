# STRETCH: implement Linear Search				
def linear_search(arr, target):
  for i in range(0,len(arr)):
    if arr[i]== target:
      print("Found target")
      return True
    print (i, "not found")

  return False
  # TO-DO: add missing code

      # not found

print(linear_search([1,7,9,4,3],3))
# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  while low<=high:
    middle = (low + high) // 2
    if target == arr[middle]:
       print("got the target")
       return True

    if target > arr[middle]:
      low =middle+ 1
      print("this is low,"+str(low))
    else:
      high = middle-1
      print("this is high"+str(high))


  # TO-DO: add missing code

  return -1 # not found

print("Btree",binary_search([1,9,12,18,24,45,47,90],12))

# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  #low=0
  #high =len(arr)-1

  middle = (low+high)//2
  print (middle)
  print(arr[middle])

  if len(arr) == 0:
     return -1 # array empty
  if target ==arr[middle]:
     return True
  if target>arr[middle]:
     #low=middle+1
     return binary_search_recursive(arr[middle+1:],target)
  else:
     return binary_search_recursive(arr[:middle],target)
  # TO-DO: add missing if/else statements, recursive calls
  return -1  # not found


print("BreEcursivetree",binary_search_recursive([1, 9, 12, 18, 24, 45, 47, 90,100],90,0,8))
