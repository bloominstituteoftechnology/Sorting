# Selection sort: first item in array checks second item to see if first item is larger or not. If first item is larger,
# first item and second item switch positions in array. Then the recently switched item checks itself in the same manner
#  against all the other numbers until switched and then that switched number does the same.



# # # TO-DO: Complete the selection_sort() function below
# # def selection_sort( arr ):
# #     # loop through n-1 elements
# #     for i in range(0, len(arr) - 1):
# #         cur_index = i
# #         smallest_index = cur_index
# #         # TO-DO: find next smallest element
# #         # (hint, can do in 3 loc)
# #         # TO-DO: swap
# #     return arr
#


arr = [7, 4, 9, 2, 6, 3, 0, 8, 5, 1]

def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        print('****************************\n')
        cur_index = i
        smallest_index = cur_index
        print(f'First for loop current index {cur_index}')
        print(f'First for loop smallest index {smallest_index}')
        for j in range((i+1), len(arr)):
            print('*****SECOND FOR LOOP*****')
            smallest_index_element = arr[smallest_index]
            compared_item = arr[j]
            print(f'Second for loop current j index {j}')
            print(f'Smallest index element {smallest_index_element}')
            print(f'Second for loop compared index element {compared_item}')
            if smallest_index_element > compared_item:
                print('*****IF STATEMENT*****')
                small = arr[j]
                larger = arr[smallest_index]
                print(f'If statement Small = {small}; Larger = {larger}')
                arr[smallest_index] = small
                arr[j] = larger
                print(f'If statement Array = {arr}')
                print(f'j at end of if statement = {j}')


    return arr

print(selection_sort(arr))

# NO PRINT STATEMENT VERSION
def bubble_sort(arr):
    # Create temporary items 1 and 2 (one per compared item)
    # If item 2 is smaller than item 1, item 2 is swapped to the left of item 1
    for i in range(len(arr)):
        for z in range(len(arr)):
            while z < (len(arr) - 1):
                left = arr[z]
                right = arr[z + 1]
                for m in range(len(arr)):
                    if (left > right) and ((z + 1) < (len(arr) - 1)):
                        arr[z] = right
                        arr[z+1] = left
                        z += 1
                        left = arr[z]
                        right = arr[z+1]
                        if (left > right) and ((z + 1) == (len(arr) - 1)):
                            arr[z] = right
                            arr[z + 1] = left
                            left = arr[z]
                            right = arr[z + 1]
                            z += 1
                        else:
                            break
                    if (right > left) and ((z + 1) < (len(arr) - 1)):
                        z += 1
                        left = arr[z]
                        right = arr[z+1]
                    if right == left:
                        pass
                else:
                    break
            break
    return arr

print(bubble_sort(arr))




# def bubble_sort(arr):
#     # Create temporary items 1 and 2 (one per compared item)
#     # If item 2 is smaller than item 1, item 2 is swapped to the left of item 1
#     for i in range(len(arr)):
#         # print(arr[9])
#         # j = i
#         # print('********************')
#         # print(f'i @ beginning = {i}')
#         # print(f'j @ beginning = {j}')
#         for z in range(len(arr)):
#             # j = z
#             # print(f'J ({j}) = Z ({z})')
#             # print(f'Z = ({z})')
#             while z < (len(arr) - 1):
#                 left = arr[z]
#                 # print(arr)
#                 # print(j)
#                 right = arr[z + 1]
#                 # print(f'while loop #{j}')
#                 # print(f'Pre-Swap: temp-Left = ({left}); temp-Right = ({right})')
#                 # print(f'Pre-Swap: array-Left = ({arr[j]}); array-Right = ({arr[j + 1]})')
#                 for m in range(len(arr)):
#                     if (left > right) and ((z + 1) < (len(arr) - 1)):
#                         # print('if left > right: swap')
#                         # print(f'if statement #{j}')
#                         arr[z] = right
#                         arr[z+1] = left
#                         z += 1
#                         left = arr[z]
#                         # print(left)
#                         # print(arr[j])
#                         # print(arr[j+1])
#                         right = arr[z+1]
#                         # print(arr)
#                         # print('^Swapped array print ^')
#                         # print(f'Post-Swap: temp-Left = ({left}); temp-Right = ({right})')
#                         # print(f'Post-Swap: array-Left = ({arr[j]}); array-Right = ({arr[j + 1]})')
#                         if (left > right) and ((z + 1) == (len(arr) - 1)):
#                             arr[z] = right
#                             arr[z + 1] = left
#                             left = arr[z]
#                             right = arr[z + 1]
#                             # print(arr)
#                             # print(left)
#                             # print(right)
#                             # print(f'j = {j}')
#                             # print('WOW')
#                             z += 1
#                         else:
#                             # print('break')
#                             break
#                     if (right > left) and ((z + 1) < (len(arr) - 1)):
#                         # print('if right > left: move on to next')
#                         # print(f'if statement #{j}')
#                         z += 1
#                         left = arr[z]
#                         right = arr[z+1]
#                         # print(arr)
#                         # print('^Same array print ^')
#                         # print(f'No-Swap: temp-Left = ({left}); temp-Right = ({right})')
#                         # print(f'No-Swap: array-Left = ({arr[j]}); array-Right = ({arr[j + 1]})')
#                     if right == left:
#                         # print('Right == Left')
#                         pass
#                 else:
#                     # print('Else statement')
#                     break
#             break
#         # print(f'i @ end = {i}')
#         # print(f'j @ end = {j}')
#     return arr
#
# print(bubble_sort(arr))

#
# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):
#
#     return arr

