# Iterative Sorting w/ Brady Fukumoto

## BIG-O and TIME COMPLEXITY
### How does the performance of your code scale based on the size of your inputs?
- e.g. Speed of your code with 5 users vs 5000. 

#### Big-O Cheat Sheet: [https://www.bigocheatsheet.com/]

## Performance Curve Shapes:

### :one: O(1) || O(log n): :arrow_right:

The time complexity of this is going to be `O(1)`, which means that it is `constant`. The reason why this is constant(constant time operation) is because we're returning a pointer to the start of our list. This doesn't necessarily mean it would be faster to return a smaller list vs. a bigger list--all you're returning is one operation, which is returning the start of the list, regardless of the size of the list.

    import math
    import random
    import time
    from datetime import datetime

    animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat', 'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']


    # returns the names of all animals
    def getAnimals():
        return animals

### :two: O(n):  :arrow_upper_right:

This time complexity is going to be `O(n)` because as the list gets bigger, the number of operations get bigger, which increases the time spent running the function based on the number of inputs. Such speed dependent on the inputs would depict a linear Big-O shape.

To be concise: Our inputs is size `n`, and for each of these inputs, the function runs. The number of operations we need to do dependent on the number of inputs; therefore, the performance curve will be a linear shape.

Even if the function has multiple lines of codes run, the rule is, you always drop the constant coefficient. It just matters *how many* times the code is run rather than the complexity of the code. (e.g. even though the function has 5 lines of code it wouldn't be `O(5n)` but still would be `O(n)` because we care about the shape of the curve and not necessarily the complexity of it.)

    # returns the number of all animals
    def countAnimals():
        num_animals = 0
        for animal in animals:
            num_animals +=1
        return num_animals

In this function we set `lowercase_animals` as the animals array, and then set `animal_index` variable to 0. After, we create a loop: for each animal in animals, we reassign each element in the `lowercase_animals` array as the lower case version. After this operation, we run the line `animal_index += 1` which then reassigns the value of `animal_index` as the current value + 1. After the end of the loop is finished, we return the `lowercase_animals` array with the new assignments.

All in all, this function would still be an `O(n)` regardless of the number of operations. 

    # returns each animal with all letters lowercase
    def getLowerCaseAnimals():
        lowercase_animals = animals
        animal_index = 0
        for animal in animals:
            lowercase_animals[animal_index] = lowercase_animals[animal_index].lower()
            animal_index += 1
        return lowercase_animals

For the following function, we are comparing each element in the array with the input given. The time complexity of this case would still be `O(n)` even when it depends if the item is in our list or not. Therefore when refering to the `Big-O` of the following case, one is asking, interchangeably, the average and worst case curve--the order of complexity. 

Given that the average case is `O(n/2)` which is the same as `O(0.5 *n)`, drop the constant coefficent and you get `O(n)`

    # Given the name of an animal--
    # Return True if that animal is in the list, False, otherwise
    def hasAnimal(animal_name):
        num_comparisons = 0
        for animal in animals: 
            num_comparisons += 1
            print("comparisons: {num_comparisons}")
            if animal == animal_name:
                return True
        return False


    # Given the name of an animal, 
    # Return the animal's index if that animal is in the list, -1 otherwise
    def findAnimal(animal_name):
    for animal in animals:
        if animal == animal_name:
            return animal_index +=1
    return -1


    # Shuffle the order of the stored animals
    def shuffleAnimals():
        num_animals = countAnimals()
        for i in range(num_animals):
            random_i = random.randrange(num_animals)
            temp_storage = animals[i]
            animals[i] = animals[random_i]
            animals[random_i] = temp_storage

Overall, for `O(n)`, "For every item in the list, you do something," which usually means a for loop. Thus, a huge indicator of an `O(n)` would be a for loop.

### :three: O(n^2): :arrow_heading_up:

The number of operations within functions with a Big-O of `O(n^2)` would mean that, depending on the number of inputs, the number of operations grow exponentially.

In the following function, we are looping through every element in the list, and then for every element looped through, we are looping through it again in order to print out all the possible combinations. Therefore, the Big-O would be `O(n) * O(n)` which is `O(n^2)`.

    animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat', 'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']

    def printAnimalPairs():
        num_operations = 0
        for animal1 in animals:
            for animal2 in animals:
                num_operations += 1
                print (f"{num_operations}: {animal1} - {animal2}")

### :four: O(n^3): 
    











