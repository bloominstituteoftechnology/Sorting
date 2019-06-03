# TO-DO: Complete the selection_sort() function below
def selection_sort(list):
    # loop through n-1 elements
    for i in range(0, len(list) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index + 1, len(list)):
            if list[j] < list[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        list[cur_index], list[smallest_index] = list[smallest_index], list[cur_index]

    return list


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(list):
    swap = True
    # this line is required to account for empty lists
    swapped = False
    # loop will keep running until a no-swap pass through the list is completed
    while swap == True:
        for i in range(1, len(list)):
            if i == 1:
                # resets swap tracker to False at the beginning of each pass through list
                swapped = False
            if list[i] < list[i - 1]:
                list[i], list[i - 1] = list[i - 1], list[i]
                # if a swap occurs on this particular comparison, the pass gets credit for a swap
                swapped = True
        # when a no-swap pass is complete, this will "tell" the while loop to stop running
        swap = swapped
    return list


# STRETCH: implement the Count Sort function below
def count_sort(list, max=-1):
    for i in list:
        if i < 0:
            return "Error, negative numbers not allowed in Count Sort"

    count = [0 for i in range(max)]

    for i in range(1, len(list)):
        count[list[i]] = count[list[i]] + 1

    for i in range(2, max):
        count[i] = count[i] + count[i - 1]

    for i in range(len(list), 1):
        list[count[list[i]]] = list[i]
        count[list[i]] = count[list[i]] - 1

    print(count)
    return list


nums = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

print(count_sort(nums))
