# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # find next smallest element
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr


# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):

    for i in range(1, len(arr)):
        # print(arr[i])
        index = i 
        while index > 0 and arr[index - 1] > arr[index]:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index = index - 1

    return arr

# print(insertion_sort([1,5,6,2,3]))


# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):

    for i in range(0, len(arr) - 1):
        swapped = False

        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if swapped == False:
            break

    return arr

# print(bubble_sort([1,5,6,2,3]))


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    # create a new array the size of 0 to the biggest number in arr filled with 0's
    counting = [0 for i in range(0, max(arr) + 1)]

    # loop over existing arr and the index 
    # of the ammount in the new_arr += 1
    for i in range(0, len(arr)):
        counting[arr[i]] += 1

    # modify the counting array by adding the previous counts
    for i in range(0, len(counting) -1):
        counting[i + 1] = counting[i] + counting[i + 1]

    # place the objects in their correct positions and
    # decrease the count by one
    places = [0 for i in range(0, len(arr))]
    for i in range(0, len(arr)):
        temp = arr[i]
        places_index = counting[temp] - 1
        places[places_index] = temp
        counting[temp] -= 1
    
    return places

# print(count_sort([1,5,1,6,2,26,5,3,3,3,3,12]))