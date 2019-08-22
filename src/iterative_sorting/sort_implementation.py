# Here the elements are swapped each time.
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i

        while j > 0 and arr[j-1] > arr[j]:
            temp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = temp
            j -= 1

    return arr


# Here the element is swapped at last.
def insertion_sort2(books):
    for i in range(1, len(books)):
        temp = books[i]
        j = i

        while j > 0 and temp < books[j - 1]:
            books[j] = books[j - 1]  # scoot books over to make room
            j -= 1

        # j is now the index of where we want to place the book
        books[j] = temp

    return books


# Using for loop. This goes through all iterations.
def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
        print(f'After iteration {i}')
        print(arr)

    return arr


# Using while loop. This goes through the iteration only when there
# was a swap happened previously. This is more effective.
def bubble_sort2(arr):
    swapping_occured = True

    while swapping_occured:
        swapping_occured = False

        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                swapping_occured = True
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
    return arr


# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        # TO-DO: swap
        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp

    return arr


# Implementation based on https://www.youtube.com/watch?v=7zuGmKfUt7s
def count_sort(arr, maximum=-1):
    if maximum == -1:
        maximum = max(arr)

    # Create a count list to hold occurance
    count_list = [0] * (maximum+1)

    # print(count_list)

    # Check and update the occurance
    for i in range(len(arr)):
        count_list[arr[i]] += 1

    # print(count_list)

    # Find relative position
    for i in range(0, len(count_list)-1):
        count_list[i+1] += count_list[i]

    # print(count_list)

    # Create output array with len same as input arr
    output = [None] * len(arr)

    for i in range(len(arr)):
        # Find element's value in arr
        value = arr[i]
        # Find value's index from count_list
        index = count_list[value]
        # Put value in output array based on index
        output[index-1] = value
        # Decrement the index in count_list
        count_list[value] -= 1

    return output


arr = [1, 4, 1, 2, 7, 5, 2]
print(arr)
print(count_sort(arr))


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# arr1 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(f'Input: {arr1}')
print(f'Output: {selection_sort(arr1)}')
