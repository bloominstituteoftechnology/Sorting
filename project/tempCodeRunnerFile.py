merged_arr[i] = arrB[b]
        b +  = 1
    elif b >= len(arrB):# all elements in arrB have been merged
        merged_arr[i] = arrA[a]
        a +  = 1
    elif arrA[a] < arrB[b]:# next element in arrA smaller, so add to final array
        merged_arr[i] = arrA[a]
        a +  = 1
    else:# else, next element in arrB must be smaller, so add it to final array
        merged_arr[i] = arrB[b]
        b +  = 1