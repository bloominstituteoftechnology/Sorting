# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
    # loop through n-1 elements

    for i in range(0, len(arr) - 1):    # range(3) = 0, 1, 2 range(1, 3) = 1, 2
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        # ret.append(smallest_index) 
        for j in range(i+1, len(arr)):    
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        print(arr)
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr
# print(selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))



# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):
    for i in range(0, len(arr) - 1):
        left = arr[0:i+1]
        val = arr[i + 1]
        if val < left[-1:][0]:
            for ind, j in enumerate(left):

                if val < j:
                    arr[i + 1], arr[ind] = arr[ind], arr[i + 1]

    return arr

# print(selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))
print('*' * 10)
# print(insertion_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))

# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):

    for i in range(0, len(arr) - 1):
        curr_val = arr[i]
        next_val = arr[i + 1]
        print(curr_val, next_val)
        if curr_val > next_val:
            arr[curr_val], arr[next_val] = arr[curr_val], arr[next_val]
    print(arr)
    return arr
print(bubble_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr