
# constructs a randomized array of length 'size'
# each element is randomly selected from range 0 up to 'max'
def create_array(size=10, max=50):
    from random import randint
    return[randint(0,max) for _ in range(size)]



# # TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(a, b):
    c = [] # final output array
    a_idx,b_idx=0,0
    while a_idx < len(a) and b_idx < len(b):
        if a[a_idx] < b[b_idx]:
            c.append(a[a_idx])
            a_idx += 1
        else:
            c.append(b[b_idx])
            b_idx += 1
    if a_idx == len(a):
        c.extend(b[b_idx:])
    else:
        c.extend(a[a_idx:])
    return c
# two 'sorted' arrays for testing
a = [1,3,5]
b = [2,4,6]

print(merge(a,b))
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(a):
    # a list of zero/one elements is sorted because there's nothing to sort
    if len(a) <= 1:
        return a
    # we have to split the array in half and do a recursive call on each half
    midpoint = int(len(a)/2)
    left, right = merge_sort(a[:midpoint]), merge_sort(a[midpoint:])

    # merge the sorted sub-arrays
    return merge(left,right)

test1 = create_array()
print(test1)
merged = merge_sort(test1)
print(merged)

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
