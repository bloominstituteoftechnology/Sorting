test_list = [3,44,38,5,47,15,36,26,27,2,46,4,0,19,50,48]

# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # num = [n for n in arr]
        # print(num)
        cur_index = i
        # print(f' current: {arr[cur_index]}')
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for x in range(i + 1, len(arr)):
            if arr[smallest_index] > arr[x]:
                smallest_index = x     
                # print(arr[smallest_index])
        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr

# print(selection_sort(test_list))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0, len(arr)):
        for x in range(0, len(arr) - 1):
            if arr[x] > arr[x + 1]:
                arr[x], arr[x + 1]= arr[x + 1], arr[x]
    return arr

# print(bubble_sort(test_list))
'''
def bubble_sort(arr):
    #define your loop length
    length = len(arr) - 1
    #define a way to break your main loop
    sorted = False
    while not sorted:
        #if list is sorted, this will break out of the main loop
        sorted = True
        #loop through each element
        for i in range(0 , length):
            # compare the current element to its adjacent element
            if arr[i] > arr[i + 1]:
            #keep outer loop going
                sorted = False
								# swap elements
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
		#return your sorted list
    return arr
'''
# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr