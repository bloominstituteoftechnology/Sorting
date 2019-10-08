# TO-DO: Complete the selection_sort() function below 
















def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        print(f"i:{i}")
        new_arr = arr[smallest_index + 1:]
        for item_count in range(len(new_arr)):
            if new_arr[item_count] < arr[i]:
                arr.insert(cur_index, arr.pop(cur_index + item_count + 1))
                print(f"arr{arr} \n")

        if arr[i] > arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp

        # print(f"{i} --->>>> {arr}")
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        # TO-DO: swap

    return arr

arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

print(f"\nstart ->> {arr}\n\n")

a = selection_sort(arr)
print(f"\n\nend ->>>>{a}")


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr