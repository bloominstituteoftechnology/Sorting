# Complete the selection_sort() function below in class with your instructor
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # find next smallest element
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr


# my_arr = [2,5,9,7,4,1,3,8,6]
# print(my_arr)
# arr = selection_sort(my_arr)
# print(my_arr)



# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):
     # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
        tmp = arr[i] 
        j = i-1
        
        while j >=0 and tmp < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = tmp

    return arr
print('insertion sort:')
my_arr = [2,5,9,7,4,1,3,8,6]
print(my_arr)
arr = insertion_sort(my_arr)
print(my_arr)

# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr