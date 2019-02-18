# Complete the selection_sort() function below in class with your instructor
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

# try it out
my_arr = [2,5,9,7,4,1,3,8,6]
print(my_arr)
arr = selection_sort(my_arr)
print(my_arr)


# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):
    # separate the first element from the rest of the array
    # think about it as a sorted list of one element
    #first_element = arr.pop(0)

    # for all other indices, beginning with [1]:
    for index in range(1, len(arr)):
        # copy the item at that index into a temp variable
        cur_index = arr[index]
        prev_index = index - 1
        # iterate to the left until you find the correct index in the "sorted" part of the array at which this element should be inserted
        while prev_index >= 0:
            if cur_index < arr[prev_index]:
                # shift items over to the right as you iterate
                arr[prev_index + 1] = arr[prev_index]
                arr[prev_index] = cur_index
                prev_index = prev_index - 1

            else:
                break

        # when the correct index is found, copy temp into this position
    return arr

# try it out
arr = [2,5,9,7,4,1,3,8,6];
print(arr);
arr = insertion_sort( arr );
print(arr);


# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr