# 1. What is the Goal? -- define what you expect to be returned, if anything
# 2. What are the Steps? -- write down all the steps to get there
# 3. Fringe Cases? -- as you define steps you will uncover fringe cases: what are they?
# 4. First pass solution? -- code out all the steps and fringe cases, don't worry about improving run time or space efficiency, just get it working!
# 5. Refactoring to a second pass solution / Final answer -- improve readability, improve time complexity, improve space complexity

# Integer Pairs
# Write a function integerPairs to find and print out all pairs of integers within an input array which sum up to a specified input value k.

# There are multiple ways to do this, depending upon whether you want to favor runtime or space.

# Example:

# input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11

# expected output: '6 5', '7 4', '8 3', '9 2', '10 1'
# Analyze the time and space complexity of your solution.

# Goal - strings of integer pairs which sum to a given integer
# Steps - loop through array, if array[i] + array[x] = y, add them to the string to print. Outer loop needs to be time-locked, inner loop is a while loop that runs until second item = len - 1


def integerPairs(arr, num):
    # declare an empty list in which to stick successful pairs
    printString = []  # O(1)
    
    # loop over array to check each integer against all integers to the right of it
    for i in range(0, len(arr)-2):  # O(n)
        
        # declare an index variable for the comparison
        next_index = i + 1  # O(1)
        
        # loop over all indexes to the right of that which is currently i, conditional on next_index being less than the length of the array
        while next_index <= len(arr)-1:  # O(n)
            
            # check to see if the integers sum to num
            if arr[i] + arr[next_index] == num:  # O(1)
                
                # if they do, stick them together into a string and then pop them in the array above
                printString.append(
                    str(arr[i]) + ' ' + str(arr[next_index]))  # O(1)
                
                #increment the comparison variable to check the next item in the list
                next_index += 1  # O(1)

            # in the case the integers don't sum
            else:
                
                # increment the comparison variable to check the next item in the list
                next_index += 1  # O(1)

        # while loop will close when comparison variable is greater than list length, for loop will go to next item in the list
    
    # When for loop completes, print the resulting array
    print(', '.join(printString))  # O(1)


integerPairs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11)
