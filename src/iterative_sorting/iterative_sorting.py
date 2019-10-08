# TO-DO: Complete the selection_sort() function below 
















def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        new_arr = arr[i + 1:]
        new_arr_count = -1
        for item_count in range(cur_index , len(new_arr) ):
            # print(f"{item_count} \n {cur_index} - {len(arr[cur_index:])}")
            
            if new_arr[item_count] < arr[smallest_index]:
                print(f"{new_arr[item_count]} < {arr[smallest_index]} ")
                new_arr_count = item_count
                break
                

        print(f"{new_arr[new_arr_count]} found at {new_arr_count}")

        # arr.pop(cur_index + new_arr )
        arr.insert(cur_index, arr.pop(cur_index + new_arr_count + 1))


        # print(f"{i} --->>>> {arr}")
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        # TO-DO: swap

    return arr

arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

print(f"\nstart ->> {arr}\n")

a = selection_sort(arr)
print(f"\n\nend ->>>>{a}")


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr