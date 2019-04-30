# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):  # O(n)
        cur_index = i  # O(1)
        smallest_index = cur_index  # O(1)
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):  # O(n)
            if arr[j] < arr[smallest_index]:  # O(1)
                smallest_index = j  # O(1)
        temp = arr[cur_index]  # O(1)
        arr[cur_index] = arr[smallest_index]  # O(1)
        arr[smallest_index] = temp  # O(1)

        # Python Version for swap
        # arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    # TO-DO: swap

    return arr  # O(1)

# selection_sort = O(n) = O(n)*( O(1) + O(1) + ( O(n) + O(1) + O(1) ) + O(1) + O(1) + O(1)) = O(n^2) Worst Case

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    swapped = True  # O(1)
    while swapped is True:  # O(n)
        swapped = False  # O(1)
        print(arr)
        for i in range(1, len(arr)):  # O(n)
            if arr[i - 1] > arr[i]:  # O(1)
                temp = arr[i]  # O(1)
                arr[i] = arr[i-1]  # O(1)
                arr[i-1] = temp  # O(1)
                swapped = True  # O(1)
        print(swapped)
    return arr

# bubble_sort = O(n) = O(1) + ( O(n) * O(1) * ( O(n) * O(1)*5 ) ) = O(n^2)

# Recursive version
# def bubble_sort(arr):
#     swapped = False
#     for i in range(0, len(arr) - 1):
#         if arr[i+1] < arr[i]:
#             arr[i], arr[i+1] = arr[i+1], arr[i]
#             swapped = True
#     if swapped:
#         return bubble_sort(arr)
#     return arr

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):
    main_arr = []
    result_arr = []
    max_value = 0
    for j in range(0, len(arr)):
        if type(arr[j]) is str:
            return None
        elif arr[j] > max_value:
            max_value = arr[j]
    for z in range(0, max_value + 1):
        main_arr.append(0)
    for i in range(0, len(arr)):
        num = arr[i]
        if num >= maximum:
            main_arr[num] += 1
        else:
            return "Error, negative numbers not allowed in Count Sort"
    # print(main_arr)
    for w in range(0, len(main_arr)):
        print(main_arr[w])
        while main_arr[w] > 0:
            result_arr.append(w)
            main_arr[w] -= 1
    print(max_value)
    # print(main_arr)
    # print(result_arr)
    return result_arr

import random

# print(count_sort([1, 5, 8, 4, 2, 9, 6, 0, 7, 5, "tyoe"]))
# print(random.sample(range(200), 50))
print(selection_sort(random.sample(range(200), 50)))