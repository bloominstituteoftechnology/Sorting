# TO-DO: Complete the selection_sort() function below 
















def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        i_count = smallest_index
        while i_count < len(arr[1:]):
            print(arr[i_count])


            i_count += 1
            # if arr[i_count] < arr[smallest_index]:
            #          print(arr[i_count])


        # for item_count in range(arr[1:]):
        #     if item < arr[smallest_index]:
        #         print(arritem, end=',')
        #         arr.insert(0, arr.pop(item_count))
        #         break

        print(f"{i} --->>>> {arr}")
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        # TO-DO: swap

    return arr

arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(f"arr ->> {arr}")
a = selection_sort(arr)


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr