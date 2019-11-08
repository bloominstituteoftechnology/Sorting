def iterative_search(array, target):
    for item in array:
        if item == target:
            return True
        return False

def recursive_search(array, target):
    #base case
    if len(array) == 0:
        return False
    #move towards the base case
    
    