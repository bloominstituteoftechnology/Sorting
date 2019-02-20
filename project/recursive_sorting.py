### helper function
def merge(a, b):
    c = []
    a_indx, b_indx = 0, 0
    while a_indx < len(a) and b_indx < len(b):
        if a[a_indx] < b[b_indx]:
            c.append(a[a_indx])
            a_indx += 1
        else:
            c.append(b[b_indx])
            b_indx += 1
    if a_indx == len(a):
        c.extend(b[b_indx:])
    else:
        c.extend(a[a_indx:])
    return c

def merge_sort(a):
    if len(a) <= 1:
        return a

    left, right = merge_sort(a[:len(a)//2]), merge_sort(a[len(a)//2:])

    return merge(left, right)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# TO-DO: implement the Quick Sort function below USING RECURSION
def quick_sort( arr, low, high):
    
    return arr

print(quick_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
