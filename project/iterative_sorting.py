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
    for idx, el in enumerate(arr[:-1]):
            for i in range(0, len(arr) - 1):
                curr_val = arr[i]
                next_val = arr[i + 1]
                if curr_val > next_val:
                    temp = curr_val
                    arr[i] = next_val
                    arr[i + 1] = temp
    return arr
print(bubble_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    empty = [0] * 10

    ret = [0] * (len(arr) + 1)
    for ind, el in enumerate(empty):
        for e in arr:
            if e == ind:
                empty[ind] +=1

    for ind, el in enumerate(empty):
        if ind != 0:
            prev_ind = ind - 1
            empty[ind] += empty[prev_ind]

    for ind, el in enumerate(arr): 
        if el < 0:
            return 'Error, negative numbers not allowed in Count Sort'
        empty_val = empty[el]
        ret[empty_val] = empty_val - 1
        empty[el] -= 1
    return ret[1:]
print(count_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))
# print(count_sort([1, 4, 1, 2, 7, 5, 2]))
