# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through all elements
    for i in range(len(arr)):
        # flag to see if item i has been inserted in sorted array
        replaced = False
        # loop through the already sorted part of the list
        for j in range(i+1):
            # if item i has already been inserted
            if replaced:
                # move items to the right
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
            elif arr[j] > arr[i]:
                # if this is where the item should be inserted
                # then insert it and save item to arr[i]
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
                replaced = True
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    changes = True
    while changes:
        changes = False
        for i in range(len(arr)-1):
            j = i+1
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                changes = True

    return arr


# STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr