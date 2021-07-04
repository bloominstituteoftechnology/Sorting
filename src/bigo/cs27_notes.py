# search

def linear_search(l, value):

    for i in range(len(l)):
        if i == value:
            return True

    return False

def binary_search(l, value):
    if len(l) <= 1:
        pass

    # define first and last indices
    first = 0
    last = len(l) - 1

    # variable to store if found
    found = False

    # when the first item of the list is not the last item
    # and found is not True
    while first <= last and not found:
        print(1)
        middle = ( first + last ) // 2

        if value == l[middle]:
            found = True

        else:
            if value < l[middle]:
                last = middle - 1
            else: 
                first = middle + 1
    
    return found


# insertion sort

def insertion_sort(l):
    # separate first element, think of it as sorted


    # for all other indices, starting at 1
    for i in range(1, len(l)):

        # put current number in a temp var
        temp = l[i]

        # look left, until we find position
        j = i
        while j > 0 and temp < l[j-1]:
            l[j] = l[j-1]
            j -= 1

            # as we look left, shift items right

        # when left is smaller than temp, or we're at zero, put at this spot
        l[j] = temp

    return l

l = [3,4,6,1,2,9,4,6,7,0,5]
l2 = sorted(l)
print(l)
value = 4
print('linear')
print(linear_search(l2, value))
print('binary')
print(binary_search(l2, value))
print('insertion sort')
print(f'list: {l}')
print(insertion_sort(l))


