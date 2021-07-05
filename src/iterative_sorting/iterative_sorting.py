# # TO-DO: Complete the selection_sort() function below
# # select the smallest element in the collection
# 	# startsmall = min(arr)
# 	# startsmall = arr.index(startsmall)
# 	# print(startsmall)
# 	# arr[0],arr[startsmall] = arr[startsmall], arr[0]
# 	# print(arr)


# def selection_sort(arr):
#     # loop through n-1 elements
#     for i in range(0, len(arr) - 1):
#         cur_index = i
#         smallest_index = cur_index
#         # TO-DO: find next smallest element
#         # (hint, can do in 3 loc)
#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[smallest_index]:
#                 smallest_index = j
#         # TO-DO: swap
#         if smallest_index != cur_index:
#             arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

#     return arr

# print(selection_sort([5,4,10,1,3,9,7,2,6,8]))

# # TO-DO:  implement the Bubble Sort function below


# def bubble_sort(arr):
#     for i in range(0, len(arr)-1):
#         for j in range(0, len(arr)-1-i):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

#     return arr

# print(bubble_sort([5,4,10,1,3,9,7,2,6,8]))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    count = [0,0,0,0,0,0,0,0,0,0]
    print(f'origina arr {arr}')
    for i in range(0, len(arr)):
        count[arr[i]] += 1
    print(f'count {count}')
    # print(f'callback {add_up(count)}')
    count2= add_up(count)   #[0, 2, 4, 4, 5, 6, 6, 7, 7, 7]
    print(f'count2 {count2}')

      #Last step is confusing. I think it can be solved using hashtables, which i have no idea how to use. 
    placeholderindex = 0
    for nums in range(0, len(count)):
        while count[nums] > 0:
            arr[placeholderindex] = nums
            placeholderindex += 1
            count[nums] -= 1
    print(f'in while loop {count}')
  
    return arr

    
def add_up(count):
    newcount =[]
    cum=0
    for nums in count:
        cum += nums
        newcount.append(cum)
    # print(f' inside new function {newcount}')
    return newcount

    
    # for a in range(0, len(answer)):
    #     answer[newcount[a]] += 1
    

    # return newcount
    
print(f'arr output {count_sort([1,4,1,2,7,5,2])}')





















# for i in range(1,6):
#     print('outer', i)
#     for j in range(1,6):
#         print('inner', j, end='/t')
#     print('')






# ============================================



# def n_demo(n):
#     print(n)
#     if n == 0:
#         return
#     #recursive case
#     n_demo(n-1)

# print(n_demo(3))

# def two_n_demo(n):
#     print(n)
#     if n==0:
#         return
#     two_n_demo(n-1)
#     two_n_demo(n-1)
#     two_n_demo(n-1)

    
# def divide_n_demo(n):
#     print(n)
#     if n<= 1:
#         return

#     divide_n_demo(n/2)
#     divide_n_demo(n/2)

# print(divide_n_demo(3))

# def partition(data):
#     left=[]
#     right=[]
#     pivot=data[0]

#     for val in data[1:]:
#         if val <= pivot:
#             left.append(val)
#         else:
#             right.append(val)
#     return left, pivot, right


# def quick_sort(numbers):
#     #base case
#     if len(numbers) <= 1:
#         return numbers
    
#     left, pivot, right = partition(numbers)
#     #recursive step
#     return quick_sort(left) + [pivot] + quick_sort(right)


# print(quick_sort([5,9,3,7,2,8,1,6]))

