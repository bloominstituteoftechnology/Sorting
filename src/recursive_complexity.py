total_times_count = 0

def count_down(n):
    global total_times_count
    total_times_count += 1

    if n == 0:
        return
    
    count_down(n - 1)
    count_down(n - 1)

def half(n):
    if n <= 1:
        return
    
    half(n / 2)

# O(log n)

# O(c^n)
# O(n)

#(2^5)
# 2^10

count_down(5)
print(total_times_count)