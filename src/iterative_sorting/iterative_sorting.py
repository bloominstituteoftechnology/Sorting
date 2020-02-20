# TO-DO: Complete the selection_sort() function below 
test_list = [8, 2, 5, 4, 1, 3]

# print(test_list)

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        print("start:")
        print(arr)
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i, len(arr)): 
            if arr[j] < arr[cur_index] and arr[j] < arr[smallest_index]:
                smallest_index = j
                # print("smallest:")
                # print(smallest_index)
                # print(arr[smallest_index])
                # print("current:")
                # print(cur_index)
                # print(arr[cur_index])
        # TO-DO: swap
        if cur_index != smallest_index:
            temp = arr[cur_index]
            arr[cur_index] = arr[smallest_index]
            arr[smallest_index] = temp
        print("end:")
        print(arr)
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    cursor = 0
    flag = True
    swap = False
    while flag == True and cursor < len(arr):
        start = arr.copy()
        print("cursor:")
        print(cursor)
        for i in range(cursor, len(arr) - 1):
            if arr[i + 1] < arr[i]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                swap = True

        print("start:")
        print(start)

        print("end:")
        print(arr)

        if swap == False and cursor < len(arr):
            cursor += 1
        if start == arr:
            flag = False
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

# print(selection_sort(test_list))
print(bubble_sort(test_list))