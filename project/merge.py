
def merge(a, b):
    c = []
    a_indx, b_indx = 0, 0
    while a_indx < len(a) and b_indx < len(b):
        if a[a_indx] < b[b_indx]:
            c.append(a[a_indx])
            a_indx += 1
        else:
            c.append(b[b_indx])
            b_indx += 1
    if a_indx == len(a):
        c.extend(b[b_indx:])
    else:
        c.extend(a[a_indx:])
    return c

def merge_sort(a):
    if len(a) <= 1:
        return a

    left, right = merge_sort(a[:len(a)//2]), merge_sort(a[len(a)//2:])

    return merge(left, right)

print(merge_sort([-2, 1, 0, 4, -6, 7, 3, -9, 5]))
