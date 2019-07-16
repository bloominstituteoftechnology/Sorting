# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1): #O(n)
        cur_index = i# O(1)

        for i in range(cur_index +1, len(arr)):#0(n)
            comparison_index = i#(O(1))

            if arr[cur_index] < arr[comparison_index]:#O(1))
                pass#O(1))
            
            elif arr[cur_index] >= arr[comparison_index ]:#O(1))
                arr[cur_index], arr[comparison_index] =  arr[comparison_index], arr[cur_index]#O(2))?

 #all in all 6n^2 +1 ??

    return arr#O(1))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr