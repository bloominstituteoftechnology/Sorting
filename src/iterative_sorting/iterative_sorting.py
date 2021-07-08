# TO-DO: Complete the selection_sort() function below












def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b



def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        finished = True
        new_arr = arr[smallest_index + 1:]

        for item_count in range(len(new_arr)):
            if new_arr[item_count] < arr[i]:
                arr.insert(cur_index, arr.pop(cur_index + item_count + 1))
                finished = False

        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i + 1], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    has_swapped = False

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i+1] = arr[i + 1], arr[i]
            has_swapped = True
            print(f"\n{arr}")

    if has_swapped:
        return bubble_sort(arr)
    else:
        return arr




# print(x)


# print(f"\nend   ->> {x}\n\n")


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
