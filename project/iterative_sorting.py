# Complete the selection_sort() function below in class with your instructor
sort_array = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
sort_array2 = [50, 70, 80, 40, 100, 70, 110, 180, 20190, 480]

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr
print(selection_sort(sort_array))

# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):
    for i in range(0, len(arr) - 1):
        cur_value = arr[i]
        position = i

        while position > 0 and arr[position - 1] > cur_value:
            arr[position] = arr[position - 1]
            position = position - 1
        arr[position] = cur_value

    return arr

print ("insertion_sort iter: ", insertion_sort(sort_array))

# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):
    done = False
    while not done:
        done = True
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                done = False
    return arr

print(bubble_sort(sort_array2))

test_count_arr = [10, 7, 12, 4, 9, 13]

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    # Find the minimum and maximum numbers of the array
    min_value = min(arr)
    max_value = max(arr)
    index = [x for x in range(min_value, max_value + 1)]
    print(index)
    count = [0 for x in range(min_value, max_value + 1)]
    print(count)
    for i in index:
        if i in arr:
            print(index.index(i))
            count[index.index(i)] = count[index.index(i)] + 1
    print(count)
    sum_count = []
    totality = 0
    for k, j in enumerate(count):
        cur_index = j
        if k != len(count) - 1:
            next_index = count[k+1]
        if j > 0:
                totality = totality + cur_index
                sum_count.append(totality)
        elif j == 0:
            sum_count.append(totality)
    print("sum_count: ",sum_count)
    min_sum = min(sum_count)
    max_sum = max(sum_count)
    position = [x for x in range(min_sum, max_sum + 1)]
    print("position: ",position)
    sorted_arr = [0 for x in range(len(position))]
    print("sorted_arr: ",sorted_arr)
    for k in arr:
        sorted_arr[position.index(sum_count[index.index(k)])] = k
    print("new sorted_arr: ",sorted_arr)
    for m, l in enumerate(sorted_arr):
        arr[m] = l
    print("arr: ",arr)
    return arr

count_sort(test_count_arr)