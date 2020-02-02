import random

# 1. Runtime? O(n)
n = 1000000
m = 1000000

a = 0
b = 0
for i in range(n):
    a += random.randint(1, 10)

for j in range(n):
    b += random.randint(1, 20)

print(a)
print(b)


# 2. Runtime? O(n^2)
a = 0
for i in range(n):
    for j in range(n, -1, -1):
        a += i + j


# 3. Runtime? O(n log(n))
i = 0 
j = 0
k = 0
for i in range(n/2, n):
    j = 2
    while j <= n:
        k = k + n/2
        j *= 2