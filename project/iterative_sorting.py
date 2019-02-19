#import this
#import antigravity
# Complete the selection_sort() function below in class with your instructor
animal = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat',
          'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']


def selection_sort(arr):
    # for each element in the array ...
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # print(f'LOOP {i}')
        # print(f'arr')
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # find next smalles element after that element
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # print(f"SMALLEST ELEMENT: {arr[smallest_index]}")
        # swap that with the current element
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
        # temp = arr[i]
        # arr[i] = arr[smallest_index]
        # arr[smallest_index] = swap
        # (hint, can do in 3 loc)
        # TO-DO: swap
    # for each element in the array, find the next smallest element after i and swap it
    return arr


# print(animal)
# selection_sort(animal)
# print(animal)

# TO-DO: implement the Insertion Sort function below


# separate first element from rest of array, own array called sorted
# begin with 1, copy item at that index into temp variable, iterate to left until you find correct index of sorted array
# insert at that position of the array, shift rest of the items to the right

# animal = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat',
#           'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']

def insertion_sort(arr):
    # step through each index, i in range 1 through length of arr non inclusive, start at 1 because if starting at 0, nothing to compare to the left of index
    for i in range(1, len(arr)):
        # temp is value at each index to compare to left of or the index, which is at first arr at index of 1 then iterates to 2, 3, 4...
        temp = arr[i]
        # value directly left is initialized to j, at the beginning of comparison
        j = i-1
        # keep comparing further and further left until the beginning of arr or index of 0, not past 0 because there is no index less than 0
        while j >= 0:
            # if temp which is index, is less than the element directly left, shift temp one to the left
            if temp < arr[j]:
                # shift whatever element at j to the right if the value of index of i or temp is less than the value directly left of it
                arr[j+1] = arr[j]
                # then shift temp or element at index to the left, if value of index or temp is less than the value directly left of it
                arr[j] = temp
                # decrement j which is initially the value directly left of temp, down one value, to preform loop over again, j will now be two to the left of i then 3 and 4... if applicable
                j -= 1
                # if the temp is not less than value you are comparing it to break from the loop, no need to shift anymore values left and right
            else:
                break
    # once we are done sorting within the range we can return the sorted arr
    return arr


# def insertion_sort(arr):
#     #
#     # for index in range(1,10), start of for loop
#     for i in range(1, len(arr)):
#         #arr = d, j, h, a, c, f , i, g, e, b
#         # d,j,h,a,c,f,i,g,e,b
#         print(f"i is {i}")
#         temp = arr[i]
#         # temp = 1jackal
#         # temp = 2hippo
#         print(f"temp is {temp}")
#         j = i-1
#         #j = 0
#         #j = 1
#         print(f"j is {j}")
#         while j >= 0 and temp < arr[j]:
#             # while 0 >=0 and jackal < duck, false
#             # while 1 >=0 and hippo < jackal, true /while 0>=0 and hippo < duck, false
#             arr[j+1] = arr[j]
#             print(f"inside while loop: {arr[j+1]}")
#             # false
#             # 2 = jackal, false
#             j -= 1
#             print(f"inside while loop j: {j}")
#             # false
#             #j =0, false
#         arr[j+1] = temp
#         # arr[1] = jackal

#     return arr


insertion_sort(animal)
print(animal)

# STRETCH: implement the Bubble Sort function below


def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
