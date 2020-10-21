def quick_sort(books):
    # base case 
    if len(books) <= 1:
        return books
    
    # recursive case 
    else:
        # choose pivot (first element)
        pivot = books[0]
        # partition - smaller elements go to LHS, larger to RHS
        lhs = [b for b in books[1:] if b <= pivot]
        rhs = [b for b in books[1:] if b >= pivot]
        # quick_sort(LHS) + [pivot] + quick_sort(RHS)
        return quick_sort(lhs) + [pivot] + quick_sort(rhs)

# non-recursive (iterative)
def sum(arr):
    sum = 0
    for num in arr:
        sum += num
    return sum

# recursive 
def rec_sum(arr):
    # base case 
    if len(arr) == 1:
        return arr[0]

    # recursive 
    else: 
        return arr[0] + rec_sum(arr[1:])

arr = [2, 5, 8, 4, 1, 6]
# sum(arr)
rec_sum(arr)