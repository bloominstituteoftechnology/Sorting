 # TO-DO: Complete the selection_sort() function below
#arr=[5,3,8,2,1]
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        min = arr[i]
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range (i+1,len(arr)):
            if arr[j] <min :
               min= arr[j]
               cur_index= j

        # TO-DO: swap
        temp= arr[i]
        arr[i] = arr[cur_index]
        arr[cur_index]= temp

    return arr

print ("Sorted array",selection_sort([5,3,8,2,1]))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # outer loop that will decide how many times the process will be repeated, the number of passes, it will be len(arr-1
    for i in range(0,len(arr)-1):
        swap=0
        #get inside the inner for loop which will compare the elements and if they are not at the right position it will swap
        for j in range (0,len(arr)-1-i):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                swap=1
        if swap==0:
           break

    return arr
print ("Sorted array",bubble_sort([5,3,8,2,1]))


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1):

    d = {}
    minNum = min(arr)
    maxNum = max(arr)

    #Go through array and count frequency of each element
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    result = []
    for i in range(minNum, maxNum + 1):#For each number possible in range
        if i in d: #Check if we have seen this number. d[i] represents number of times i appeared
            while d[i]: #We need to append i di] times
                result.append(i)
                d[i] -= 1 #Reduce frequence.


    return result

print ("Sorted array",count_sort([5,3,8,2,5,2,1,3]))