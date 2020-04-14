# TO-DO: Complete the selection_sort() function below 

thing = [7, 15, 2, 58, 9]


def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        print("cur_index- ", cur_index)
        print("smallest_index-", smallest_index)
        if smallest_index <= cur_index:
            print("made it")
            cur_index += 1

        elif smallest_index > cur_index:
            smallest_index = cur_index
            cur_index += 1

        #     



        # TO-DO: swap




    return arr

print(selection_sort(thing))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    #Get first two elements 0, 1
    slot1 = 0
    slot2 = 1



    #compare 0 <= 1
    #swap if false
    #move to elements 1,2
    #repeat until there are zero swaps

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr