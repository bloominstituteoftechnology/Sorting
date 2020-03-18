# TO-DO: Complete the selection_sort() function below 

def selection_sort(l):

    # loop through n-1 elements
    for i in range(0, len(l) - 1):
        j = i

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        lowest_num = l[j]
        lowest_index = j

        for j in range(i, len(l)):
            if l[j] < lowest_num:
                lowest_num = l[j]
                lowest_index = j

        # swap the lowest with the current position
        swap_num = l[i]
        l[i] = lowest_num
        l[lowest_index] = swap_num

    return l


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr


l = [3,4,6,1,2,9,4,6,7,0,5]
print('selection_sort')
print(selection_sort(l))
