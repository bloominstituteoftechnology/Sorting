# TO-DO: Complete the selection_sort() function below 
# def selection_sort( arr ):
#     # loop through n-1 elements
#     for i in range(0, len(arr) -1):
#         cur_index = i
#         smallest_index = cur_index
#         # TO-DO: find next smallest element
#         # (hint, can do in 3 loc) 
#         print (arr)
#         for j in range(cur_index, len(arr)):
#             if arr[j] < arr[smallest_index]:
#                 smallest_index = j

#                 # TO-DO: swap
#                 arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
#     return arr

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # find next smallest element
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # swap
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
arr2 = []
arr3 = [0, 1, 2, 3, 4, 5]
# arr4 = random.sample(range(200), 50)

print(selection_sort(arr1))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swapped = True
    while(swapped == True):
        swapped = False
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                swapped = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr