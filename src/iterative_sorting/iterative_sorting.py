def selection_sort(arr):
    # arr: [50, 20, 10, 30, 40]
    # Find minimum element in arr[0,1,2,3,4] and swap it with arr[0]: 
    # 10, 20, 50, 30, 40

    # Find minimum element in arr[1,2,3,4] and swap it with arr[1]:
    # 10, 20, 50, 30, 40

    # Find minimum element in arr[2,3,4] and swap it with arr[2]:
    # 10, 20, 30, 50, 40

    # Find minimum element in arr[3,4] and swap it with arr[3]:
    # 10, 20, 30, 40, 50
    for i in range(len(arr)):
        min_val = arr[i]
        ith_val = arr[i]
        min_index = i
        for j in range(i+1, len(arr)):
            if min_val > arr[j]:
                min_val = arr[j]
                min_index = j
        arr[i] = min_val
        arr[min_index] = ith_val
    return arr

print("Selection:", selection_sort([50, 20, 10, 30, 40]))


def bubble_sort(arr):
    # Compare each element to the next:
        # if 1st > 2nd, then swap
        # if 2nd > 3rd, then swap
        # repeat for all elements
        # larger elements begin to "bubble" towards the end 
    # Repeat comparing and swapping until the array is sorted
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                jth_val = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = jth_val
    return arr

print("Bubble:", bubble_sort([50, 20, 10, 30, 40]))


# STRETCH
def count_sort(arr, maximum=-1):
    return arr