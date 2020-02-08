# TO-DO: Complete the selection_sort() function below
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)



        # TO-DO: swap


    return arr

testArr = [3, 6, 2, 7, 100, 21, 401, 1, 22, 4, 7, 5]

def insertion_sort(testArr):
    # capturing the entire range minus the first variable.  The first variable has nothing to the left to compare itself to, so its not necessary
    length_of_index = range(1, len(testArr))

    for i in length_of_index:
        # why does this need a variable? 
        value_to_sort = testArr[i]
        # why can't I just use testArr[i] instead of value_to_sort?
        while testArr[i - 1] > value_to_sort and i > 0:
            # doing a swap if the above conditions are true, this is just easy python syntax for a swap
            testArr[i], testArr[i - 1] = testArr[i - 1], testArr[i]
            # decrementing i, or it will be an infinite loop
            i = i - 1

    return testArr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # Step 1: loop through the array
    # get a variable for the length of the array
    length = len(arr)
    for i in range(length):
        # setting a variable so we can tell if anything has been swapped or not
        swapped = False
        # adding - i - 1 to the range because we don't have to compare the last item against anything
        # why do we need the -i part? Why not just - 1 to stand for the length minus 1?
        for j in range(0, length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # keeping swapped as true as long as a change was made
                swapped = True

        if swapped == False:
            # breaking the loop if we don't make a change
            break
    
    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr


# print(insertion_sort(testArr))
print(bubble_sort(testArr))
