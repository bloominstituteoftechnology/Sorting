# TO-DO: Complete the selection_sort() function below 
# loop through n-1 elements
# TO-DO: find next smallest element
# (hint, can do in 3 loc) 
# TO-DO: swap

def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[min] > arr[j]:
                min = j; 
        arr[i], arr[min] = arr[min], arr[i]
        print(arr)
        return arr
        

answer = [2, 55, 6, 77, 8, 4, 66666, 7, 2]  

selection_sort(answer)



    


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swap_occured = True
    while swap_occured:
        for i in range(len(arr)):
            for j in range(0, len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    temp = arr[j + 1]
                    arr[j + 1] = arr[j]
                    arr[j] = temp
                    swap_occured = True
                else: 
                    swap_occured = False

numbers = [3, 66, 4, 55, 42, 6, 67, 33]

bubble_sort(numbers)


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr