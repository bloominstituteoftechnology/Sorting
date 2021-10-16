# recursive way
def insertionSortRecursive(arr,n):
   # base case
   if n<=1:
      return
   # Sort
   insertionSortRecursive(arr,n-1)
   last = arr[n-1]
   j = n-2
   # move ahead
   while (j>=0 and arr[j]>last):
      arr[j+1] = arr[j]
      j = j-1
   arr[j+1]=last
# main
arr = [1,5,3,4,8,6,3,4,5]
n = len(arr)
insertionSortRecursive(arr, n)
print("Sorted array is:")
for i in range(n):
   print(arr[i],end=" ")
