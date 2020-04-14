# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
#     # loop through n-1 elements
#     # len(arr) => 5
#     # out of bounds
#     # len(arr) - 1
#     # 4 -> 3 
     for i in range(0, len(arr) - 1): 
         cur_index = i
         smallest_index = cur_index
#         # TO-DO: find next smallest element
#         # (hint, can do in 3 loc) 
#         # iterate over a range
         for j in range(cur_index, len(arr)):
             if arr[j] < arr[smallest_index]:
                 smallest_index = j

        
#         # swap
         arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

     return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    n = len(arr)

    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j] ## keep swapping the order and change the position ( 5 1 4 2 8 ) –> ( 1 5 4 2 8 ) an so on 

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    m = maximum = 0
    count = [0] * m               
    for a in arr:
        count[a] += 1             
    i = 0
    for a in range(m):           
        for c in range(count[a]): 
            arr[i] = a
            i += 1

    return arr