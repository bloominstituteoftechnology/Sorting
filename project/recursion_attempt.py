import random

myList = [random.randint(0, 1000) for i in range(0, 30)]
print(myList)


def factorial(n):
    print()
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))


def i_factorial(n):
    val = 1
    for i in range(1, n + 1):
        val *= i
    return val


print(i_factorial(5))


def merge(left, right):
    pass


def mergeSort(arr):
    left = mergeSort(arr[0: len(arr) // 2])
    right = mergeSort(arr[len(arr) // 2:])
    return merge(left, right)
