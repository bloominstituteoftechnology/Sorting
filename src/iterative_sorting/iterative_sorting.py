def selection_sort( arr ):
    for i in range(len(arr)):
        sm_i = min(enumerate(arr[i:], start=i), key=lambda x: x[1])[0]
        arr[i], arr[sm_i] = arr[sm_i], arr[i]

    return arr

def bubble_sort( arr ):
    sorted = False
    while not sorted:
        # Assume it's already sorted and look for evidence to the contrary.
        sorted = True
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr

def count_sort( arr, maximum=-1 ):
    if arr == []:
        return []

    if min(arr) < 0:
        return 'Error, negative numbers not allowed in Count Sort'

    cntArr = [0] * (max(arr)+1)

    for e in arr:
        cntArr[e]+=1

    index = 0
    for i, e in enumerate(cntArr):
        arr[index:index+e] = [i]*e
        index+=e

    return arr
