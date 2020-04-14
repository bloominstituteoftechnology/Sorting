# numbers = [9,7,6,8,5,2,1,3,4,112,0]
# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(0, len(arr)):
            # print(f"index: {i} sub-index: {j}")
            if arr[j] > arr[cur_index]:
                # print(f"{arr[j]} > {arr[cur_index]}")
                arr[i], arr[j] = arr[j], arr[i]
                # print(arr)
                smallest_index = j
                # print(f"smallest_index is now: {arr[smallest_index]}")

        # TO-DO: swap   
        # print(arr[i], arr[j])
        arr[i], arr[j] = arr[j], arr[i]
        # print(arr[i], arr[j])
        # print(arr)

    return arr

# print(selection_sort(numbers))


def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i
        while j > 0 and temp < arr[j -1]:
            arr[j] = arr[j - i]
            j -= 1
        arr[j] = temp
    return arr

# print(f"insertion sort{insertion_sort(numbers)}")

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(len(arr) -1, 0, -1):
       for j in range(i):
           if arr[j] > arr[j + 1]:
               temp = arr[j]
               arr[j] = arr[j + 1]
               arr[j + 1] = temp
    return arr

# print(f"bubble_sort{bubble_sort(numbers)}")


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr