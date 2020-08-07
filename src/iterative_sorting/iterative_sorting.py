arrOne = [17, 13, 11, 16, 19, 20, 15, 14, 12, 18]

# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
        cur_index += 1
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
             



        # TO-DO: swap




    return arr

print(selection_sort(arrOne))
# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swapped = True
    while swapped:
        swapped = False
        for index in range(len(arr)):
            if index == 0:
                continue
            if arr[index] < arr[index - 1]:
                arr[index], arr[index - 1] = arr[index - 1], arr[index]
                swapped = True

    return arr


arrOne = [17, 13, 11, 16, 19, 20, 15, 14, 12, 18]
bubble_sort(arrOne)
print(arrOne)

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr