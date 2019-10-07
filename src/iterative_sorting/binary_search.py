"""Including the notes from today's guided lecture for future reference"""

# Assume names is sorted
# Assume names is a list
def binary_search(to_find, names):
    # If the list is empty
    if len(names) == 0:
        return False
    # Cut our list in half, examine the midpoint item
    mid = len(names) // 2
    item = names[mid]
    # If the item is equal to to_find:
    if item == to_find:
        return True
    # Otherwise, if it's smaller
    elif item > to_find:
        return binary_search(to_find, names[:mid])
        # Repeat binary search on first half of the list
    # Otherwise
    else:
        return binary_search(to_find, names[mid+1:])
        # Repeat binary search on second half
​
# Iterative version of binary search
def binary_search(to_find, names):
    # Cut our list in half, examine the midpoint item
    start = 0
    end = len(names)
    while end - start > 0:
        mid = start + (end - start) // 2
        item = names[mid]
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

def insertion_sort(items):
    # Split the list into sorted and unsorted
    # For each element in unsorted...
    counter = 0
    for i in range(1, len(items)):
        print(items)
        # Insert that element into the correct place in sorted by:
        # Store the element in a temp variable
        temp = items[i]
        # Shifting all larger sorted elements to the right by 1
        j = i
        while j > 0 and temp < items[j - 1]:
            counter += 1
            items[j] = items[j - 1]
            j -= 1
        # Insert the element after the first smaller element
        items[j] = temp
        print(f"counter: {counter}")
    return items



