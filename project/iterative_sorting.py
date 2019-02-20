# Complete the selection_sort() function below in class with your instructor
#initial commit
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range (i, len(arr)):
            if arr[j]< arr[smallest_index]:
                smallest_index=j
        # TO-DO: swap
        temp=arr[cur_index]
        arr[cur_index]=arr[smallest_index]
        arr[smallest_index]=temp
    return arr



# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):
    for i in range(len(arr)):
        cur_index=i
        remember_value= arr[cur_index]
        for j in range(cur_index-1, -1,-1):
            if arr[cur_index]<arr[j]:
                arr.pop(cur_index)
                arr.insert(j, remember_value)
                print(arr)
            cur_index=j
    return arr
arr=[7,2,1,4,9,3]
print(insertion_sort(arr))
# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr