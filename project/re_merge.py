# Reimplementing Merge Sort to help me understand the
# challenge behind in-place merge sort

# update - followed youtube vid, did not work
# def create_array(size = 10, max = 50):
#     from random import randint
#     return [randint(0, max) for _ in range(size)]

# def merge(a,b):
#     c = [] # final output array
#     a_index = b_index = 0
#     # join the lists till one runs out
#     while a_index < len(a) and b_index < len(b):
#         if a[a_index]< b[b_index]:
#             c.append(a[a_index])
#             a_index += 1
#         else:
#             c.append(b[b_index])
#             b_index += 1
#     # add the list that still has items remaining to the end
#     # of the result
#     if a_index == len(a):
#         c = c + (b[b_index:])
#     else:
#         c = c + (a[a_index:])

#     return c

# a = [1,3,5]
# b = [2,4,6]
# print(merge(a, b)) # [1, 2, 3, 4, 5, 6]

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     left = merge_sort(arr[:len(arr) // 2])
#     right = merge_sort(arr[len(arr) // 2:])

#     return merge(left, right)

# test = create_array()
# print(test)
# sort = merge_sort(a)
# print(sort)


# Rerwiting provided code
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    a = 0
    b = 0
    # since arrA and arrB are already sorted, we only need
    # to compare the first element of each
    for i in range(0, elements):
        # if all elements of arrA have been merged
        if a > len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        # all elements in arrB have been merged
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        # next element in arrA smaller, so add to final array
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        # else, next element in arrB must be smaller,
        # add it to final array
        else:
            merged_arr[i] = arrB[b]
            b += 1

    return merged_arr

def merge_sort(arr):
    if len(arr) > 1:
        left = merge_sort(arr[0: len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2: ])
        arr = merge(left, right) # merge defined later
    return arr

def create_array(size = 10, max = 50):
    from random import randint
    return [randint(0, max) for _ in range(size)]

test = create_array()
print(test)
result = merge_sort(test)
print(result)