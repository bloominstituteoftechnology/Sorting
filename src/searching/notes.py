
# a factorial number (n!) is a number that is multiplied by each number less than it
# for example   7! == 7+6+5+4+3+2+1

def rec_factorial(n) :
#base case
    if n <= 1:
        return 1

#add in recursion
    return n * rec_factorial(n-1)
#multiplies n times the number "n"-1 until n-1 == 1 (basecase)

print( rec_factorial(998) )
