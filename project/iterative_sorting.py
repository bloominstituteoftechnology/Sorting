# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        # find next smallest element
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # swap

        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr

# try it out
my_arr = [2, 5, 9, 7, 4, 1, 3, 8, 6]
print("SELECTION\n" + str(my_arr))
arr = selection_sort(my_arr)
print(my_arr)


def insertion_sort( arr ):
    
    for i in range(1, len(arr)):
        temp_num = arr[i]
        temp_i = i
        for j in range(i - 1, -1, -1):
            if temp_num <= arr[j]:
                arr.pop(temp_i)
                arr.insert(j, temp_num)
                temp_i = j

    return arr

arr = [2, 5, 9, 7, 4, 1, 3, 8, 6]
print("INSERTION\n" + str(arr))
arr = insertion_sort(arr)
print(arr)


def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr