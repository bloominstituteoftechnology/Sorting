# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        index_of_min = i

        for j in range(i+1, len(arr)):
            if arr[index_of_min] > arr[j]:
                index_of_min = j

        temp = arr[i]
        arr[i] = arr[index_of_min]
        arr[index_of_min] = temp

    return arr


def insertion_sort( arr ):
# starting at second index, compare num to num to left
    for i in range(1, len(arr)):
        print(i)
        current_val = arr[i]
        position = i

        while position > 0 and arr[position - 1] > current_val:
            arr[position] = arr[position - 1]
            position -= 1
        
        arr[position] = current_val

    return arr

print(insertion_sort([1, 4, 2, 0]))





# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr