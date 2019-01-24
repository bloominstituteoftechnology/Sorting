# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        min_index=i 
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # TO-DO: swap
        temp = arr[min_index]
        arr[min_index] = arr[i]
        arr[i] = temp
    return arr

print(selection_sort(arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))



# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):
    for i in range (0, len(arr)):
        curr_num = arr[i]
        j=0
        for j in range (i-1,-2,-1):
            if arr[j] > curr_num:
                arr[j+1]=arr[j]
            else:
                break
        arr[j+1] = curr_num
    return arr

print(insertion_sort(arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))


# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr