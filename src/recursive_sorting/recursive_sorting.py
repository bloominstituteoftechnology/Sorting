# TO-DO: complete the helpe function below to merge 2 sorted arrays
r1 = [1,3,4,7,5,2] 
r2 = [8,6,5,2,1,3] 
x = r1 + r2
print(f"++++{x}")

def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    print(arrA)
    print(arrB)
    print(elements)
    merged_arr = [0]*elements
    # TO-DO
    # starting point 
    x = 0
    y = 0



    #base: 
    # for number = i in range of elements of two arrays 
    for i in range(0, elements):
        # conditionA:
        # if the first number of array A is smaller than 1st # of array B
        # put that number in a new array
        if x >= len(arrA):
            merged_arr[i] = arrB[y]
# put the rest of the numbers after the first element of new array
            y += 1 
#now you gotta do the same to arrB, pretty much flip the values
        elif y >= len(arrB):
            merged_arr[i] = arrA[x]
            x += 1
# now to the same to the actual array            
        elif arrA[x] < arrB[y]:
            merged_arr[i] = arrA[x]
            x += 1
        else:
            merged_arr[i] = arrB[y]
            y += 1

    return merged_arr


print(merge(r1, r2))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr
    halfSize = int(len(arr)//2)
    arr1 = merge_sort(arr[0: halfSize])
    arr2 = merge_sort(arr[halfSize:])
    arr = merge(arr1, arr2)

    return arr

print(merge_sort(x))

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
