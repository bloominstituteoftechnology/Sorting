# TO-DO: Complete the selection_sort() function below 












def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b



def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        #print(f"i:{i}")

        finished = True
        new_arr = arr[smallest_index + 1:]
        for item_count in range(len(new_arr)):

            if new_arr[item_count] < arr[i]:
                arr.insert(cur_index, arr.pop(cur_index + item_count + 1))
                finished = False
                
         #       print(f"arr{arr} \n")

        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i + 1], arr[i]


        # print(f"{i} --->>>> {arr}")
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        # TO-DO: swap

    return arr

arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

# print(f"\nstart ->> {arr}\n\n")

# a = selection_sort(arr)



# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    for _ in range(len(arr)):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i+1] = arr[i + 1], arr[i]
                print(f"\n{arr[i]} > {arr[i + 1]}\n{arr}")
                

    return arr


x = bubble_sort(arr)

# print(x)


# print(f"\nend   ->> {x}\n\n")


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr