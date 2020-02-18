# animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat', 'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear', 'Panda', 'Dog', 'Bat', 'Rabbit', 'Tardigrade', 'Ice Dragon', 'Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat', 'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear', 'Panda', 'Dog', 'Bat', 'Rabbit', 'Tardigrade', 'Ice Dragon']

# animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat', 'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']

# # animals.sort()

# # print(animals)

# # O(1)

# # print(animals[3])

# # animals.append("Snake")

# # 0(N)

# # for i in range(0, len(animals)):
# #     print(animals[i])

# # Print a list of every possible pair of animals in two lists?
# # )(n^2)

# # for i in range(0, len(animals)):
# #     for j in range(0, len(animals)):
# #         print(animals[i] + " -- " + animals[j])


# # n^3

# # sum = 0

# # for i in range(0, len(animals)):
# #     for j in range(0, len(animals)):
# #         for k in range(0, len(animals)):
# #             sum += 1
# #             print(animals[i] + "-" + animals[j] + "-" + animals[k])

# # print(sum)


# # def get_animal_combos(l):
# #     list_length = len(l)
# #     if list_length == 0:
# #         return [ [] ]
# #     else:
# #         animal_combos = []
# #         previous_combos = get_animal_combos( l[1:] )
# #         for combo in previous_combos:
# #             animal_combos.append( combo )
# #             animal_combos.append( combo + [l[0]] )
# #         return animal_combos

# # combos = get_animal_combos(animals)
# # print(combos)
# # print(len(combos))


# import random

# my_range = 10000000
# size = 10000000
# my_randoms = random.sample(range(my_range), size)

# # print(my_randoms)

# my_value = random.randint(0, my_range)

# # def find_value_linear(sort_list, value):
# #     for i in range(len(sort_list)):
# #         if sort_list[i] == my_value:
# #             return True

# #     return False

# # print(find_value_linear(my_randoms, my_value))

# # my_randoms.sort()
# # !!!!!!!Must be sorted for this to work
# def find_value_binary(sort_list, value):
#     # Edge case
#     if len(sort_list) == 0:
#         return False
    
#     first = 0

#     last = (len(sort_list) - 1)

#     found = False

#     # Loop until found, or check everything
#     while first <= last and not found:
#         # Find the middle of the list using integer division
#         middle = (first + last) // 2

#         # if found, update found
#         if sort_list[middle] == value:
#             found = True
#         else:
#             if value < sort_list[middle]:
#                 last = middle - 1

#             else:
#                 #Search upper half of remainder
#                 first = middle + 1

#     return found

# print(find_value_binary(my_randoms, my_value))
# print(find_value_binary(my_randoms, my_value))
# print(find_value_binary(my_randoms, my_value))
# print(find_value_binary(my_randoms, my_value))
# print(find_value_binary(my_randoms, my_value))
# print(find_value_binary(my_randoms, my_value))
# print(find_value_binary(my_randoms, my_value))
# print(find_value_binary(my_randoms, my_value))
# print(find_value_binary(my_randoms, my_value))
# print(find_value_binary(my_randoms, my_value))



my_list = [8, 2, 5, 4, 1, 3]

def insertion_sort(list_to_sort):
    # Separate the first element from the rest of the array. Think about it as a sorted list of one element.

    # For all other indices, beginning with [1]:
    for i in range(1, len(list_to_sort)):

        # a. Copy the item at that index into a temp variable
        temp = list_to_sort[i]

        # b. Iterate to the left until you find the correct index in the "sorted" part of the array at which this element should be inserted
        j = i
        while j > 0 and temp < list_to_sort[j-1]:
            print(j)
            # Shift items over to the right as you iterate
            list_to_sort[j] = list_to_sort[j - 1]
            j -= 1
        # c. When the correct index is found, copy temp into this position
        list_to_sort[j] = temp

    return list_to_sort

print(insertion_sort(my_list))
  