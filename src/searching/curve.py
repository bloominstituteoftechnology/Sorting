

arrayofitems = ['Joe', 2, 'Ted', 4.98, 14, 'Sam', 'void *', '42', 'float', 'pointers', 5006]

def arr(elements ):
    # type type checks 
    if type(elements) == type([]):  
        for i in elements:
        
            print(f"\n{i}")
    
arr("string")

a = 0
n = 1
while (a < n * n * n ):
    a = a + n * n
    print(a)

sum = 0
for i in range(n):
    j = 1
    while j < n:
        j *= 2
        sum += 1

        print(sum)