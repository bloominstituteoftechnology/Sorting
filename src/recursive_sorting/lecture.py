
#Print every number, starting at 'number
#until you reach 0
# def recurse(number):
#     if number <= 0:
#         return
#     print(number)
#     number -= 1
#     recurse(number)#when a function runs out, returns None
#     recurse(number)

# recurse(3)

#runtime complexith is O(N) 
#because it touches everything once
#2 types of recursion 12:25 pm

#every recursion problem can be iterated

# def fibonacci(n):
#     if n < 0:
#         print("Negative numbers are not valid")
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     else:
#         #Return the number plus the last number
#         return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(7))

# [5 9 3 7 2 8 1 6]

# [3 2 1][5][9 7 8 6]

# [2 1][3][5][7 8 6 9]
# [1 2][3][5][6][7 8 9]

my_list = [5, 9, 3, 7, 2, 8, 1, 6]

#Decide on a base case
def partition(data):
    left = []
    pivot = data[0]#Find the pivot point
    right = []
    for item in data[1:]:
        if item < pivot:
            left.append(item)
        else:
            right.append(item)
    return left, pivot, right

def quicksort(data):
    if data == []:
        return data

    left, pivot, right = partition(data)

    return quicksort(left) + [pivot] + quicksort(right)


print(quicksort(my_list))

#parition our data to the left and right of the pivot
#left -> smaller than pivot, right -> larger than pivot
#what if they are the same size as the pivot? Just pick one

#repeat, recurse

# import random

# def quicksort(arr):
#     if arr:
#         pivot = random.choice(arr)
#         low = [n for n in arr if n < pivot]
#         middle = [n for n in arr if n == pivot]
#         high = [n for n in arr if n > pivot]
#         return [*quicksort(low), *middle, *quicksort(high)]
#     else:
#         return []

