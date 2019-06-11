# TO-DO: complete the helpe function below to merge 2 sorted arrays

def merge( arrA, arrB ):

    result = []
    left_pointer = 0
    right_pointer = 0
    
    
    while left_pointer < len(arrA) and right_pointer < len(arrB):
        if arrA[left_pointer] <= arrB[right_pointer]:
            result.append(arrA[left_pointer])
            left_pointer = left_pointer + 1
        else:
            result.append(arrB[right_pointer])
            right_pointer = right_pointer + 1


    while left_pointer < len(arrA):
        result.append(arrA[left_pointer])
        left_pointer = left_pointer + 1


    while right_pointer < len(arrB):
        result.append(arrB[right_pointer])
        right_pointer = right_pointer + 1
    
    return result
    

   

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) < 2:
        print(f'Final {arr}')
        return arr

    midpoint = len(arr)//2
    left = merge_sort(arr[:midpoint])
    right = merge_sort(arr[midpoint:])


    print(f'merge_sort {merge(left, right)}')

    return merge(left, right)

merge_sort([1,25,-3,-9,9,100,50,24,8])



# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr

