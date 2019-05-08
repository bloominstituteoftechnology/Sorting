# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( left, right ):
    elements = len( left ) + len( right )
    output = [] #[0] * elements
    l = 0
    r = 0
    for i in range(0, elements):
        # do the comparison step
        if l >= len(left):
            # the left list is exhausted
            # we can just move everything from the right lis to the output
            output.append(right[r])
            r += 1
        elif r >= len(right):
            output.append(left[l])
            l += 1
        elif left[l] < right[r]:
            #put the left element into the output array
            output.append(left[l])
            l += 1
        else:
            output.append(right[r])
            r += 1
        
    # TO-DO
    return output 


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        left  = merge_sort(arr[0 : len(arr) // 2 ])
        right = merge_sort(arr[len(arr) // 2 :   ])
        arr   = merge(left, right)
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
def timsort( arr ):

    return arr

#O(n)
def count_down(n):
    while n >= 0:
        print(n)
        n -= 1


def count_down_recursive(n):
    print(n)
    if n <= 0:
        return
    return count_down_recursive(n-1)


print("While Loop")
count_down(10)
print("Recursive")
count_down_recursive(10)

def nth_fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return nth_fibonacci((n -1 ) + (n - 2))




"""
[5 9 3 7 2 8 1 6]
pick a pivot - 5
make a sublist of everything smaller to the left
make a sublist of everything larger to the right
iteration 1 - [3 2 1] [5] [9 7 8 6]
iteration 2 
"""

def partition(data):
    left = []
    right = []
    pivot = data[0]
    #loop through everything except for the pivot
    for number in data[1:]:
        #if smaller or equal to, put in the left hand side
        if number <= pivot:
            left.append(number)
        else:
            right.append(number)
    return left, pivot, right

def quicksort(data):
    if len(data) == 0:
        return data
    left, pivot, right = partition(data)
    return quicksort(left) +  [pivot] + quicksort(right)

quickArray = [5, 9, 3, 7, 2, 8, 1, 6]
print(quickArray)
print(quicksort(quickArray))
