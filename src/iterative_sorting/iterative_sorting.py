# TO-DO: Complete the selection_sort() function below
print('hello')
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for x in range(i+1, len(arr)):
            if arr[smallest_index] > arr[x]:
                smallest_index = x

        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    print(arr)
    return arr
a = [1,5,6,7,5,4,2]
print(selection_sort(a))
# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # not usually the best, but sometimes can me
    # n = length of the array
    n = len(arr)

    # For every item in the array
    for i in range(n):
        for j in range(0, n-i-1):
            # traverse the array from begging to end
            # and swap out if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr