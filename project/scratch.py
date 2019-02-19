# print(len([1, 2, 3]) - 1)

a = [ 5, 2, 9, 7, 4, 1, 3, 8, 6, 10 ]

def insertion_sort(arr):
    for i in range(0, len(arr) - 1):
        if arr[i] > arr[i+1]:
            a, b = arr[i], arr[i+1]
            arr[b], arr[a] = arr[a], arr[b]
        if i > 0:
            while i > 0:
                if arr[i] < arr[i-1]:
                    print(i)

                    # We swap like above.






    # a, b = array[1], array[i+1]
    # array[b], array[a] = array[a], array[b]






    # if index > arr[1]:


    # if index > arr[2]:
    #     arr[1] = arr[2]
    #     arr[2] = index
    #     index = arr[3]



    # print(f"New array :{new_array}")
    return arr


print(insertion_sort(a))

# def selection_sort(arr):
#     for i in range(0, len(arr) -1):
#         cur_index = i
#         smallest_index = cur_index
#         for k in range(cur_index, len(arr)):
#             if arr[k] < arr[smallest_index]:
#                 smallest_index = k
#     # print(arr[smallest_index])
#         temp = arr[smallest_index]
#         arr[smallest_index] = arr[cur_index]
#         arr[cur_index] = temp
#         # temp = arr[smallest_index]
#         # arr[smallest_index] = arr[cur_index]
#         # arr[cur_index] = temp
#     return arr



# print(selection_sort(a))

