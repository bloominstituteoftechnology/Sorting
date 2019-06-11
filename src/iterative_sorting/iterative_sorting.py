# TO-DO: Complete the selection_sort() function below 

numbers = []



def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        print(str(arr) + 'iloop' + str(arr[i]))
        for j in range(i, len(arr)):
            print(str(arr) + 'jloop' + str(arr[j]))
            while arr[j] < arr[i]:
                switch1 = arr[j]
                switch2 = arr[i]
                arr[i] = switch1
                arr[j] = switch2
    return arr
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
             



        # TO-DO: swap



# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swappedValues = True

    while swappedValues:
        swappedValues = False
        for i in range(0,len(arr) - 1):
            # print(arr)
            # print(arr[i + 1])
            switch1 = arr[i]
            switch2 = arr[i + 1]
            if arr[i] > arr[i + 1]:
                arr[i] = switch2
                arr[i + 1] = switch1
                swappedValues = True

    return arr



# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

    