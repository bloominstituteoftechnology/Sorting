# TO-DO: Complete the selection_sort() function below


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        for j in range(cur_index, len(arr)):
            comp_index = j
            if arr[smallest_index] > arr[comp_index]:
                smallest_index = comp_index
        # TO-DO: swap
        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp
    return arr

# # TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    newArr = arr[:]
    # loop through n-1 elements
    for i in range(0, len(newArr) - 1):
        cur_index = i
        # TO-DO: compare numbers
        for j in range(0, len(newArr)-cur_index - 1):
            first_num = j
            second_num = j + 1
            if newArr[first_num] > newArr[second_num]:
                # TO-DO: swap
                temp = newArr[first_num]
                newArr[first_num] = newArr[second_num]
                newArr[second_num] = temp
    return newArr


# # STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):
    if arr:
        occurences = [0] * (max(arr)+1)
        newArr = [0] * len(arr)
        for num in arr:
            if num < 0:
                return "Error, negative numbers not allowed in Count Sort"
            else:
                occurences[num] += 1
        accum = occurences[:]
        for i in range(1, len(accum)):
            accum[i] += accum[i-1]
            shift = accum[:-1]
            shift.insert(0, 0)
        for num in arr:
            newArr[shift[num]] = num
            shift[num] += 1
        return newArr
    else:
        return arr
