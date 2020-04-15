# TO-DO: complete the helpe function below to merge 2 sorted arrays

def merge( arrA, arrB ):
    result = []
    i = j = 0
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            result.append(arrA[i])
            i+=1
        else:
            result.append(arrB[j])
            j+=1
    result += arrA[i:]
    result += arrB[j:]


    return result

#arrA = [2,3,4,5,6,7]
#arrB = [9,10,11,12,13]
#merge(arrA, arrB)

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    #(base case) if the array is empty or lenght 1 return
    if len(arr) <= 1:
        return arr
        left = merge_sort(arr[:len(arr)//2])
        right = merge_sort(arr[len(arr)//2:])
        arr = merge(left, right)

    return arr
arr = [2,5,3,6,9,4,15,0]
merge_sort(arr)
    # TO-DO

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):

    #split here

    #find the middle of arr
    #put stuff to the left in left
    #put the stuff to the right in right

    #merge left and right

# # STRETCH: implement an in-place merge sort algorithm
#def merge_in_place(arr, start, mid, end):
    # TO-DO

   # return arr

#def merge_sort_in_place(arr, l, r):
    # TO-DO

    #return arr


# # STRETCH: implement the Timsort function below
#def timsort( arr ):

    #return arr