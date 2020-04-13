arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def bubble_sort(arr):
    # Create temporary items 1 and 2 (one per compared item)
    # If item 2 is smaller than item 1, item 2 is swapped to the left of item 1
    for i in range(len(arr)):
        # print(arr[9])
        j = i
        # print('********************')
        # print(f'i @ beginning = {i}')
        # print(f'j @ beginning = {j}')
        for z in range(len(arr)):
            j = z
            # print(f'J ({j}) = Z ({z})')
            # print(f'Z = ({z})')
            while j < (len(arr) - 1):
                left = arr[j]
                # print(arr)
                # print(j)
                right = arr[j + 1]
                # print(f'while loop #{j}')
                # print(f'Pre-Swap: temp-Left = ({left}); temp-Right = ({right})')
                # print(f'Pre-Swap: array-Left = ({arr[j]}); array-Right = ({arr[j + 1]})')
                for m in range(len(arr)):
                    if (left > right) and ((j + 1) < (len(arr) - 1)):
                        # print('if left > right: swap')
                        # print(f'if statement #{j}')
                        arr[j] = right
                        arr[j+1] = left
                        j += 1
                        left = arr[j]
                        # print(left)
                        # print(arr[j])
                        # print(arr[j+1])
                        right = arr[j+1]
                        # print(arr)
                        # print('^Swapped array print ^')
                        # print(f'Post-Swap: temp-Left = ({left}); temp-Right = ({right})')
                        # print(f'Post-Swap: array-Left = ({arr[j]}); array-Right = ({arr[j + 1]})')
                        if (left > right) and ((j + 1) == (len(arr) - 1)):
                            arr[j] = right
                            arr[j + 1] = left
                            left = arr[j]
                            right = arr[j + 1]
                            # print(arr)
                            # print(left)
                            # print(right)
                            # print(f'j = {j}')
                            # print('WOW')
                            j += 1
                        else:
                            # print('break')
                            break
                    if (right > left) and ((j + 1) < (len(arr) - 1)):
                        # print('if right > left: move on to next')
                        # print(f'if statement #{j}')
                        j += 1
                        left = arr[j]
                        right = arr[j+1]
                        # print(arr)
                        # print('^Same array print ^')
                        # print(f'No-Swap: temp-Left = ({left}); temp-Right = ({right})')
                        # print(f'No-Swap: array-Left = ({arr[j]}); array-Right = ({arr[j + 1]})')
                    if right == left:
                        # print('Right == Left')
                        pass
                else:
                    # print('Else statement')
                    break
            break
        # print(f'i @ end = {i}')
        # print(f'j @ end = {j}')
    return arr

print(bubble_sort(arr))

import random
l = list(range(10000))
random.shuffle(l)
l_copy = l.copy()

import time
start_time = time.time()
print(bubble_sort(l_copy))
end_time = time.time()
print(f'runtime: {end_time - start_time}')
