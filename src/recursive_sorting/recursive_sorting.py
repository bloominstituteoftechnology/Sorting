# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    print(arrA)
    print(arrB)
    merged_arr = [0] * elements
    # TO-DO
    # starting point 
    x = 0
    y = 0
    newArr = [0]*elements
    #base: 
    # for number = i in range of elements of two arrays 
    for i in range(0, elements):
        # conditionA:
        # if the first number of array A is smaller than 1st # of array B
        # put that number in a new array
        if(arrA[x] < arrB[y]):
            newArr[i] = arrA[x]
            x += 1 
        else:
            # put the rest of the numbers after the first element of new array
            for j in range((i+1), elements):
                newArr[j] = arrB[y]
                y += 1

            break    
    #now you gotta do the same to arrB, pretty much flip the values
    for j in range((i+1), elements):
        newArr[j] = arrA[x]
        x += 1
        break
              
    return merged_arr

r1 = [1,3,4,7,5,2] 
r2 = [8,6,5,2,1,3] 
print(merge(r1, r2))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# basically tim sort is just a sorter array thats morfed later 
def timsort( arr ):

    return arr
