n = [None] * 1000

# O(1)
def simple_function(n):
    return n

simple_function(n)

# O(n)
def make_another_array(n):
    inner_array = []

    for i in n:
        inner_array.append(i)

    return inner_array

make_another_array(n)

# O(n^2)
def make_matrix(n):
    matrix = []

    for item in n:
        row = []

        for i in n:

            row.append(i * 2)

        matrix.append(row)

        
def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n - 1)

factorial(3)
# 3 * 2 * 1 * 1