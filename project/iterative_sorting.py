# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
    #     # (hint, can do in 3 loc) 
    #     for i in range( len( aList ) ):
    # least = i
    # for k in range( i + 1 , len( aList ) ):
    #   if aList[k] < aList[least]:
    #     least = k
 
    # swap( aList, least, i )     



        # TO-DO: swap




    return arr


# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):
    if len(arr) == 0:
        return arr
    for i in range(len(arr)):
        j = i + 1
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            
    return arr

print(insertion_sort([3,4,2,1,5,0]))

# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):
    if len(arr) == 0:
        return arr

    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

print(bubble_sort([3,4,2,1,5,0]))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    if len(arr) == 0:
        return arr
    counter = [0] * (max(arr) + 1) 
    #print(counter)
    for i in arr:
        if arr[i] >=0:
            counter[i] += 1
            #print(counter)
        else:
            return "Error, negative numbers not allowed in Count Sort"
 
    k = 0
    for i in range( len( counter ) ):
      while 0 < counter[i]:
        arr[k] = i
        k += 1
        counter[i] -= 1
     
    return arr
    
print(count_sort([1,0,4,3,2,1,4,3,2,4,3,4,4]))
