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

    # TO-DO: swap

    return arr  # O(1)

# selection_sort = O(n) = O(n)*( O(1) + O(1) + ( O(n) + O(1) + O(1) ) + O(1) + O(1) + O(1)) = O(n^2) Worst Case

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    swapped = True # O(1)
    while swapped is True: # O(n)
        swapped = False # O(1)
        print(arr)
        for i in range(1, len(arr)): # O(n)
            if arr[i - 1] > arr[i]: # O(1)
                temp = arr[i] # O(1)
                arr[i] = arr[i-1] # O(1)
                arr[i-1] = temp # O(1)
                swapped = True # O(1)
        print(swapped)
    return arr

# bubble_sort = O(n) = O(1) + ( O(n) * O(1) * ( O(n) * O(1)*5 ) ) = O(n^2)

# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr


print(bubble_sort([2, 4, 3, 0, 5, 6, 7, 8, 9, 1, 10, 0]))
