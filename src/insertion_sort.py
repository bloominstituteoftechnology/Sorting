def insertion_sort(items):
    # Split the list into sorted and unsorted
    # For each element in unsorted...
    counter = 0
    for i in range(1, len(items)):
        # Insert that element into the correct place in sorted
        # Store the elements in a temp variable
        temp = items[i]
        # Shifting all larger sorted elements to the right by 1
        j = i
        while j > 0 and temp < items[j - 1]:
            print('**********************')
            counter += 1
            print(items)
            items[j] = items[j - 1]
            j -= 1
            print(items)
            # Insert the element after the first smaller element
            items[j] = temp
            print(items)
            print(f'Counter = {counter}')
    return items


l = [7, 4, 9, 2, 6, 3, 0, 8, 5, 1]

insertion_sort(l)