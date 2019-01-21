# Complete the selection_sort() function below in class with your instructor
def selection_sort(arr):
    for end in range(len(arr) - 1, 0, -1):
        position_of_max = 0

        for current in range(position_of_max, end + 1):
            if arr[current] > arr[position_of_max]:
                position_of_max = current

        # Swap
        temp = arr[end]
        arr[end] = arr[position_of_max]
        arr[position_of_max] = temp
    return arr


# TO-DO: implement the Insertion Sort function below
def insertion_sort(arr):
    for x in range(1, len(arr)): # 0 is already sorted, so start at 1
        c_value = arr[x]  # Grab the current value
        position = x  # Track our current position

        while position and arr[position - 1] > c_value: # Keep shifting until the previous isn't greater than the c_value
            arr[position] = arr[position - 1]  # Switch our current value with the previous value
            position = position - 1  # Update the position to start over (after the switch occurred)

        arr[position] = c_value # After any shifting, we've found the correct position, set it to the current value
    return arr


# STRETCH: implement the Bubble Sort function below
def bubble_sort(arr):
    for _ in range(0, len(arr) - 1):
        for x in range(0, len(arr) - 1):
            current_element = arr[x]
            next_element = arr[x + 1]

            if next_element < current_element:
                arr[x] = next_element
                arr[x + 1] = current_element

    return arr
# O(n^2)

# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    return arr
