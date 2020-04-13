# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index+1, len(arr)):

            if arr[smallest_index] > arr[j]:
                smallest_index = j
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

        # TO-DO: swap

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    
    for i in range(0, len(arr) - 1):

        # print(cur_index, arr[cur_index], right_index, arr[right_index])
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(arr)

    return arr


# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr

arr = [5,2,3,1,4,7,9,8,0]

# selection_sort(arr)
print(bubble_sort(arr))