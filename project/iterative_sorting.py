# Complete the selection_sort() function below in class with your instructor
# slection sort
# First look through all the cards and find the smallest.
# then move the card to the correct positions in the dataset. Swap it with whatever is at the far left.
#repeat this sequence till things are done
# Look for the next smallest card.
# Don't have to look at the smallest.
# move it to the correct spot



import random
def selection_sort( arr ):
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for k in range(cur_index, len(arr)):
            if arr[k] < arr[smallest_index]:
                smallest_index = k
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp
    # loop through n-1 elements
    # for i in range(0, len(arr) - 1):
    #     cur_index = i
    #     # Find the smallest card
    #     # we pick the first index. We call that one the smallest
    #     smallest_index = cur_index
    #     for i in range(0, len(arr) -1):
    #         for k in range(0, len(arr) -1):
    #             if arr[k] < arr[smallest_index]:
    #                 smallest_index = k
    #     temp = arr[smallest_index]
    #     arr[smallest_index] = arr[cur_index]
    #     arr[cur_index] = temp
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        # TO-DO: swap
    return arr


a = [random.randint(0, 100) for i in range(0, 100)]
# print(selection_sort(a))

# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):
    # for each element after the first
    for i in range(1, len(arr)):
        current_element = arr[i]
        k = i - 1
        while k >= 0 and current_element < arr[k]:
            arr[k + 1] = arr[k]
            k -= 1
        arr[k+1] = current_element
        # find the right spot for the element in the sorted sub array on the left
        # insert it there 
            # Store the current element.
            # walk backward through the sublist shifint elemeents to the right by 1
            # until we reach a smaller element then put he curren tlement in that place

    return arr

# import random

# a = [random.randint(0, 100) for i in range(0, 100)]
# print(insertion_sort(a))

# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):
    pass

    # return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    pass

    # return arr
