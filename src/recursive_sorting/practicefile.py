# def countdown(num):
#   if num == 0:
#     return
  
#   print(num)
#   countdown(num-1)
    
# countdown(10)


# def to_int(txt):
#   if type(txt) == int:
#     print('already int')  
#   elif type(txt) == str:
#       return f'num: {int(txt)}' 
  

# print(to_int('21'))

# def to_str(num):
#   if type(num) == str:
#     print('already str')
#   elif type(num) == int:
#       return f'str: {str(num)}'

# print(to_str(37))

# def fibonacci(num):
#     if num < 2:
#         return 1
#     else:
#         return fibonacci(num - 1) + fibonacci(num - 2)

# print(fibonacci(8))

# print(9//2)
#============================================

# def helper(arr):
#   a= arr[:len(arr)//2]
#   b= arr[len(arr)//2:]

#   return  split(a,b, arr)



# def split(a,b, arr):
#   splitarr = []
#   if len(arr) !=len(splitarr):
    
 
#   a = a[:len(a)//2]
#   if len(a) == 1:
#     splitarr.append(a)

#   b = b[len(a)//2:]
#   if len(b) == 1:
#     splitarr.append(b)
#   split(a,b, arr)

# print(helper([1,2,3,4,5,6,7,8]))


# =========================================
# def chunk(array, size):
#   if len(array) == 0: 
#     return []
#   firstChunk = array[:size]
#   print(firstChunk)
 
#   if len(firstChunk) == 0: 
#     return array
  
#   return [firstChunk ].append(chunk(array[size:len(array)], size))
  
# print(chunk([1,7,5,9,4,3,5,2,6,8],1))