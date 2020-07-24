def insertionSort(unsort_arr):
    for i in range(1, len(unsort_arr)):
        curr_ele = unsort_arr[i]
        j = i-1

        while j >= 0 and curr_ele <  unsort_arr[i]:
            unsort_arr[j + 1] =unsort_arr[j]
            j - j-1
        unsort_arr[j+1] = curr_ele