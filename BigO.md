# Steps for Calculating Big O()

1. Things in sequence in a block: add big Os
2. Things in loops: multiply big O by the big O of the body
5. Drop constant factors
6. Keep only the dominant term (largest time complexity term dominates)

def first(l):     # O(3) = O(3 * 1) = O(1) Rule 5: "drop constant factors"
    a = l[0]     # O(1)
    a += 1       # O(1)
    return a     # O(1)


def print_all(l):           # O(n * 1) = O(n)
    for i in l:             # O(n)
        print(i)            # O(1)

def something(l):                  # O(n)
    a = l[0]                       # O(1)
    a += 1                         # O(1)
    for i in range(len(l) / 2):    # O(n / 2) Rule 5, so this becomes O(n)
        a += i                     # O(1)
        print(a)                   # O(1)
    print(a)                       # O(1)
    return a