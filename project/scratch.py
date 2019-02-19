# print(len([1, 2, 3]) - 1)

# a = [ 5, 2, 9, 7, 4, 1, 3, 8, 6, 10 ]
a = [item for item in range(30)]


# a.sort()
#binary sory.

def binary_search(arr, target):
    first = 0
    last = len(arr) -1
    while first <= last:
        midpoint = (first + last) // 2
        if arr[midpoint] == target:
            return arr[midpoint]
        else:
            if target < arr[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return arr

print(binary_search(a, 13))
def binary_search1(arr, target): 
    pass
    # step 1. we find the midpoint.
    # midpoint = len(arr) // 2
    # while len(arr) > 3:
    # # We check to see if midpoint is equal to target.
    #     if target == arr[midpoint]:
    #         return target
    #     # we check to see which side target is on
    #     else:
    #         if target > arr[midpoint]:
    #             print('on the left')
                
    #             # midpoint = len(arr[midpoint:]) // 2
    #             # The pop is just to reduce the array to end the loop.
    #             arr.pop()
    #             # arr = arr[midpoint:]
    #             # arr = arr[:midpoint]
    #             # print(f"Left midpoint {midpoint} ")
    #         else:
    #             print('on the left')
                
    #             # midpoint = len(arr[:midpoint]) // 2
    #             arr.pop()
    #             print(len(arr))
    #             # # arr = arr[:midpoint]
    #             # print(f"Right midpoint {midpoint}")
                # arr = arr[midpoint:]

    # 3. We set that as a new array.
    # 3. We find the midpoint.
    # 4. Then we check wich side the target is on until we find the target.
    # midpoint = len(arr) // 2
    # new_array = arr 
    # while len(new_arry) > 1:


# while len(a) > 1:
#     midpoint = len(a) // 2
#     a = a[:midpoint]
#     print(a)


    # if arr[midpoint] == target:
    #     return target
    # elif target > arr[midpoint]:
    #     print('on the right')
    # else:
    #     new_array = arr[:midpoint]
    #     while len(new_array) > 1:
    #         midpoint = len(new_array) // 2
    #         if new_array[midpoint] == target:
    #             return target
    #         elif target > new_array[midpoint]:
    #             print('it on right')
    #         else:
    #             new_array = new_array[]
    #             print('it on left')




        # we want to check which half the array is in.
        # Then we want to find the midpoint of the half.
        # Check to see which side the number is on.
        # Then split that in half 
        # So while that 


# print(binary_sort(a, 1))
# def insertion_sort(arr):
#     for i in range(0, len(arr) - 1):
#         if arr[i] > arr[i+1]:
#             # a, b = arr[i], arr[i+1]
#             arr[i+1], arr[i] = arr[i], arr[i+1]
#         if i > 0:
#             temp_index = i
#             while temp_index > 0:
#                 if arr[temp_index] < arr[temp_index-1]:


#                     print(i)

                    # We swap like above.






    # a, b = array[1], array[i+1]
    # array[b], array[a] = array[a], array[b]






    # if index > arr[1]:


    # if index > arr[2]:
    #     arr[1] = arr[2]
    #     arr[2] = index
    #     index = arr[3]



    # print(f"New array :{new_array}")
    # return arr


# print(insertion_sort(a))

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

