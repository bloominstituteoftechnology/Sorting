import random

# arr4 = random.sample(range(200), 50)
# # print(arr4)
arr4 = [56, 65, 97, 59, 4, 86, 173, 181, 141, 83, 92, 114, 198, 199, 40, 119, 166, 189, \
28, 149, 169, 37, 131, 179, 107, 78, 120, 85, 30, 146, 121, 35, 23, 62, 106, 89, 127, \
126, 185, 46, 117, 10, 174, 6, 102, 84, 187, 52, 18, 103]
# TO-DO: Complete the selection_sort() function below

def selection_sort(arr):
    # loop through n-1 elements
    for i in range(1, len(arr)):
        # print('i', i, arr[i])
        # print(arr)
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                temp = arr[j - 1] 
                arr[j-1] = arr[j]
                arr[j] = temp
            else:
                break
    return arr

print(selection_sort([5,1,5,9,7, 8]))
# # print(selection_sort([1, 5, 8, 4]))
# # arr2 = [5,1,5,9,7]
# arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7, 97, 100, 101, 101, 105, 107, 112, 113, 115]
# print(selection_sort(arr4))
# print(selection_sort(arr1))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    m = 1
    first = True
    while m > 0 or first:
        first = False
        m = 0
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i+1]:
                temp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = temp
                m += 1

    return arr


# print(bubble_sort([5,1,5,9,7]))

# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    for i in range(0, len(arr)):
        if arr[i] < 0:
            return "Error, negative numbers not allowed in Count Sort"        
    for i in range(0, len(arr) - 1):
        a = [arr[i], i]
        for j in range(i + 1, len(arr)):
            if arr[j] < a[0]:
                a = [arr[j], j]
        if a[1] != i:
            arr[a[1]] = arr[i]
            arr[i] = a[0]
    return arr

# arr3 = [97, 100, 101, 101, 105, 107, 112, 113, 115]
# arr5 = [1, 5, -2, 4, 3]
# print(count_sort(arr5))
