# TO-DO: Complete the selection_sort() function below 

input_array = [2, 54, 11, 1, 145, 8]

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for index in range(i, len(arr)):
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
            print(arr[index])
            if arr[index] <= arr[smallest_index]:
                smallest_index = index
        
    
        # TO-DO: swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[i]
        arr[i] = temp
        print(arr[i])

    return arr

print(selection_sort(input_array))
# input_array = [2, 54, 11, 1, 145, 8]

# # TO-DO:  implement the Bubble Sort function below
# def bubble_sort( arr ):
#     for i in range(0, len(arr)):
#         for index in range(1, len(arr)):
#             current = arr[index]
#             previous = arr[index - 1]
        
#             if previous <= current:
#                 continue
#             else:
#                 arr[index] = previous
#                 arr[index - 1] = current
    
#     return arr

# print(bubble_sort(input_array))


# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr