# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # loop through the list to the right of i
        for j in range (i, len(arr)): 
            #check each item against the smallest_index
           if arr[j] < arr[smallest_index]:
               # if the item at is smaller than the one at smallest index, set smallest index to j
               smallest_index = j
        
        # TO-DO: swap
        # once the index of the smallest item in the list has been found, assign its value to arr[i] from the outer loop

        big = arr[i]
        small = arr[smallest_index]
        arr[i] = small
        arr[smallest_index] = big



    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0, len(arr)-1):
        # set index variables to compare to eachother
        current_index = i
        next_index = current_index + 1
        # run the comparison through the loop till the last item
        while next_index <= len(arr) - 1:
            # compare 
            if arr[current_index] > arr[next_index]:
                # swap values and increment value of index variablees 
                big = arr[current_index]
                little = arr[next_index]
                arr[current_index] = little
                arr[next_index] = big
                current_index += current_index
                next_index += next_index
            else:
                # if no swap needed, just increment value of index variables
                current_index += current_index
                next_index += next_index
                
    return arr

print (bubble_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
