# Assume names is sorted
# Assume names is a list
def binary_search(to_find, names):
    # Cut our list in half, examine the midpoint item
    start = 0
    end = len(names)
    while end - start > 0:
        mid = start + (end - start) // 2
        item = names[mid]
        print(start)
        print(mid)
        print(end)
        print('***')
        # If the item is equal to to_find:
        if item == to_find:
            return True
        # Otherwise, if it's smaller
        elif item > to_find:
            end = mid - 1
            # Repeat binary search on first half of the list
        # Otherwise
        else:
            start = mid + 1
            # Repeat binary search on second half
    return False


names = ['Jack', 'Jill', 'Joe', 'James', 'Jessica', 'Jones', 'Jeremy', 'Jamie']


def sorting(list):
    list.sort()
    return list


names = sorting(names)

print(names)
to_find = ['Jamie']

print(binary_search('Jamie', names))