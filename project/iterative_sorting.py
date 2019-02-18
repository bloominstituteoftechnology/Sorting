# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # fins next smallest element after that element
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        # swap that with current element
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
        # temp = arr[i]
        # arr[i] = arr[smallest_index]
        # arr[smallest_index] = temp

    # For each element in the array, find the next smallest element and swap it
    return arr


# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):

    for x in range(1, len(arr) -1):
        index = x
        value = arr[x]

        while index > 0 and arr[index-1]>value:
            arr[index]=arr[index-1]
            index = index-1

        arr[index]=value

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