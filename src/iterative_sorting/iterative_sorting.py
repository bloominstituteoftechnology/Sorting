# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(2, len(arr)):
        print('i', i, arr[i])
        print(arr)
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                temp = arr[j - 1] 
                arr[j-1] = arr[j]
                arr[j] = temp
            else:
                break
    return arr

# print(selection_sort([5,1,5,9,7, 8]))
print(selection_sort([1, 5, 8, 4]))
# arr2 = [5,1,5,9,7]
# arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# print(selection_sort(arr1))
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

    return arr
