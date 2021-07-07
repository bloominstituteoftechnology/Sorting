def quicksort(items):
    # 0. base case
    if len(items)<= 1:
        return items
    
    # 1. Select the last element as the pivot
    pivot = items[-1]
    left = []
    right = []
    
    for i in range(len(items)-1):
        item = items[i]

        if item < pivot:
            left.append(item)
        else:
            right.append(item)
    return quicksort(left) + [pivot] + quicksort(right)

def inplace_quicksort(items):
    # 0. base case
    if len(items)<= 1:
        return items
    
    # 1. Select the last element as the pivot
    pivot = items[-1]
    left = []
    right = []
    
    for v in items[1:-1]:
        
        if v <= pivot:
            left.append(v)
        else:
            right.append(v)
    return left + [pivot] + right


test = ([x for x in range(1,10)])

test = test[::-1]

print(test)
print(inplace_quicksort(test))


