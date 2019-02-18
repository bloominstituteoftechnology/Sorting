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

def insertion_sort(arr):
    # sorted_arr = [arr[0]]
    # print(sorted_arr)
    for i in range(1, len(arr)):
        temp = arr[i]
        # print(temp)
        j = i-1
        while j >= 0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
    # sorted_arr = [arr[0]]
    # print(sorted_arr)
    # for i in range(1, len(arr)):
    #     # print(arr[i])
    #     temp = arr[i]
    #     reversed = sorted_arr[::-1]
    #     for j in range(0, i):
    #         # if duck < jackal
    #         if temp > reversed[j]:
    #             sorted_arr.insert(arr[j], temp)
    # sort_arr = [arr[0]]
    # for i in range(1, len(arr)):
    #     temp = arr[i]
    #     #iterate the sorted array in reverse
    #     j = i-1
    #     while j>=0 and temp < arr[j]:

    return arr


insertion_sort(animal)
print(animal)

# STRETCH: implement the Bubble Sort function below


def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
