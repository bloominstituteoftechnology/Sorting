# Complete the selection_sort() function below in class with your instructor
sort_array = [5, 7, 8, 4, 10, 7, 11, 18, 2019, 48]
sort_array2 = [50, 70, 80, 40, 100, 70, 110, 180, 20190, 480]

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr
print(selection_sort(sort_array))

# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):
    for i in range(1, len(arr) - 1):
        cur_value = arr[i]
        position = i

        while position > 0 and arr[position - 1] > cur_value:
            arr[position] = arr[position - 1]
            position = position - 1
        arr[position] = cur_value

    return arr

print (insertion_sort(sort_array))

# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):
    done = False
    while not done:
        done = True
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                done = False
    return arr

print(bubble_sort(sort_array2))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    
    return arr