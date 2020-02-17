# TO-DO: Complete the selection_sort() function below
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # cur_index = i
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                # we're just constantly updating the smallest value with indexes that are smaller until we've looped through everything
                smallest_index = j

        # we don't do the swapping until we have looped through the entire list!  
        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]


    return arr

testArr = [5, 2, 6, 3, 8, 10, 13, 3, 4, 6, 9, 100, 2, 0, 1]

def insertion_sort(arr):
    # Step 1: loop through the array, the first index in the array is going to be our "sorted" bit
    # don't need minus 1 because range is (inc, exclusive)
    for i in range(1, len(arr)):
        print('i', i)
    # Step 2: Take the indexes (except the last one) after the current array and move them to the left until they are at the appropriate position in the sorted part
        while arr[i] < arr[i - 1] and i > 0:
            print('swap', i)
            temp = arr[i]
            arr[i] = arr[i - 1]
            arr[i - 1] = temp

            i = i - 1

    # Step 3:

    return arr

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

# def insertion_sort(arr):
#     for i in range(1, len(arr)):

#         # while position is at least 1 and
#         while i > 0 and arr[i - 1] > arr[i]:
#             arr[i] = arr[i -1]

#     print(arr)




# # TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

# insertion_sort(arr1)

# print(insertion_sort(testArr))
# print(bubble_sort(testArr))
# print(selection_sort(testArr))tele
# print(standup(test, 'ball'))
# print(bubble_sort(testArr))