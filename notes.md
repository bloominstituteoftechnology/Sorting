# Iterative Sorting w/ Brady Fukumoto

Why do we need to sort? Well, the short answer to that is that it allows us to search at an optimized, effective speed. In this unit we cover the Big-O, which is the perfomance of your code based on the size of your inputs, and how it is used to made definitive decisions on the way you code.

## BIG-O and TIME COMPLEXITY
### How does the performance of your code scale based on the size of your inputs?

 [<img src="https://i.imgur.com/E53oSiV.jpg"/>](https://www.bigocheatsheet.com/)

### Terms:
- **log** means **logarithm**
- A **logarithm** is a quantity representing the power to which a fixed number (the base) must be raised to produce a given number.
- **log** with a base 2 _basically_ means:
    - if you have `2^x = num`
    - `log2(2^x)` = `log2(num)`
    - Any log of the log's base returns a value of 1
    - so cross out ~~`log2(2)`~~ `^x` = `log2(num)`, which isolates `x` and removes it as an exponential
    - resulting in `x = log2(num)`    

## Performance Curve Shapes:

### :one: O(1) || O(log n): :arrow_right:

The time complexity of this is going to be `O(1)`, which means that it is `constant`. The reason why this is constant(constant time operation) is because we're returning a pointer to the start of our list. This doesn't necessarily mean it would be faster to return a smaller list vs. a bigger list--all you're returning is one operation, which is returning the start of the list, regardless of the size of the list.
```python
    import math
    import random
    import time
    from datetime import datetime

    animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat', 'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']


    # returns the names of all animals
    def getAnimals():
        return animals
```

### :two: O(n):  :arrow_upper_right:

This time complexity is going to be `O(n)` because as the list gets bigger, the number of operations gradually gets bigger, which increases the time spent running the function based on the number of inputs. Such speed dependent on the inputs would depict a linear Big-O shape.

To be concise: Our inputs is size `n`, and for each of these inputs, the function runs. The number of operations we need to do dependent on the number of inputs; therefore, the performance curve will be a linear shape.

Even if the function has multiple lines of codes run, the rule is, you always drop the constant coefficient. It just matters *how many* times the code is run rather than the complexity of the code. (e.g. even though the function has 5 lines of code it wouldn't be `O(5n)` but still would be `O(n)` because we care about the shape of the curve and not necessarily the complexity of it.)
```python
    # returns the number of all animals
    def countAnimals():
        num_animals = 0
        for animal in animals:
            num_animals +=1
        return num_animals
```
In this function we set `lowercase_animals` as the animals array, and then set `animal_index` variable to 0. After, we create a loop: for each animal in animals, we reassign each element in the `lowercase_animals` array as the lower case version. After this operation, we run the line `animal_index += 1` which then reassigns the value of `animal_index` as the current value + 1. After the end of the loop is finished, we return the `lowercase_animals` array with the new assignments.

All in all, this function would still be an `O(n)` regardless of the number of operations. 
```python
    # returns each animal with all letters lowercase
    def getLowerCaseAnimals():
        lowercase_animals = animals
        animal_index = 0
        for animal in animals:
            lowercase_animals[animal_index] = lowercase_animals[animal_index].lower()
            animal_index += 1
        return lowercase_animals
```
For the following function, we are comparing each element in the array with the input given. The time complexity of this case would still be `O(n)` even when it depends if the item is in our list or not. Therefore when refering to the `Big-O` of the following case, one is asking, interchangeably, the average and worst case curve--the order of complexity. 

Given that the average case is `O(n/2)` which is the same as `O(0.5 *n)`, drop the constant coefficent and you get `O(n)`
```python

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
```

Overall, for `O(n)`, "For every item in the list, you do something," which usually means a for loop. Thus, a huge indicator of an `O(n)` would be a **for loop**.

### :three: O(n^2): :arrow_heading_up:

The number of operations within functions with a Big-O of `O(n^2)` would mean that, **depending on the number of inputs, the number of operations grow exponentially.**

In the following function, we are looping through every element in the list, and then for every element looped through, we are looping through it again in order to print out all the possible combinations. Therefore, the Big-O would be `O(n) * O(n)` which is `O(n^2)`.
```python
    animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat', 'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']

    def printAnimalPairs():
        num_operations = 0
        for animal1 in animals:
            for animal2 in animals:
                num_operations += 1
                print (f"{num_operations}: {animal1} - {animal2}")
```

#### O(n^3): 

Similarly, `O(n^3)` would have the same logic of time complexity when increasing the number of combinations.
```python
    # Prints a list of all possible animal triples
    def printAnimalTriples():
        num_operations = 0
        for animal1 in animals:
            for animal2 in animals:
                for animal3 in animals:
                    num_operations += 1
                    print(f"{num_operations}: {animal1} - {animal2} - {animal3}")
                    
```

### :four: O(2^n): :arrow_up:

The following function uses a recursive strategy in order to return a list of all the possible combinations in the passed in list. First, you check if the array length is empty. If it is, return an empty array. If it isn't, grab the list from the index of 1 onwards, call the function recursively, then loop over the previousCombos array and append the first element, then the element with the list index of 0. After the list is thoroughly processed, you would get the full amount of combination in the return animalCombos array.
```python

    # Given a list,
    # Return a list of all possible combination of animals
    def getListOfAnimalCombos(list):
        list_length == len(list)
        if list_length == 0:
            return [ [] ]
        else:
            animalCombos = []
            previousCombos = getListOfAnimalCombos( list[1:] )
            for combo in previousCombos:
                animalCombos.append( combo )
                animalCombos.append( combo + [list[0]] )
            return animalCombos
```

### :five: O(n!) :heavy_exclamation_mark: :arrow_up:

N factorials are explosively bad. In the following case, the passed in animal list would output to `10 * 9 * 8 * 7 * 6 * 5....` until the end of the list. The total number of arrangements would exceed three million.
```python
    # Given a list,
    # Return a list of all possible arrangements of list items
    def getAllArrangements(list):
        if list_length <= 1:
            return [list]
        else:
            arrangements = []
            previousArrangements = getAllArrangements( l[1:] )
            for previousArrangement in previousArrangements:
                for i in range(len(previousArrangement) + 1):
                    arrangements.append( previousArrangement[i:] + [l[0]] + previousArrangement[0])
            return arrangements
```

### Application:

Let's compare a function that returns the length of a list. In the following function we're looping over the array in order to count the list. It would then be an `O(n)`.
```python

    # Given a list
    # Return the list's length 
    # O(n)
    def getLengthOfList(l):
        list_length = 0
        for i in l:
            list_length += 1
        return list_length
```

Now, how do we make this into a Big-O of `O(1)`, which is way more efficient? To optimize the previous array, we could track whenever there's an addition or removal in regards to the array. This is called **Amortization**. 

Amortization is where you store a counter inside--storing metadata. So with an addition or removal of an element, the counter decreases or increases, which is essentially only one operation instead of looping through the whole list again, resulting in an `O(1)` operation.
```python

    def getLengthOfList(l):
        return len(l)
```

Here's an example of a function used to time the runtime of various functions.
```python

    def printFunctionRuntime():
        state_time = datetime.now()
        x = getAllArrangements(animals)
        # x = getAllArrangements(animals_10 + ["Kangaroo"])
        end_time = datetime.now()
        print (end_time - start_time)
```

## Insertion Sort:

A simple sorting technique that scans the sorted list, starting at the beginning, for the correct insertion point for each of the items from the unsorted list. Similar to the way people manually sort items(e.g. playing 13, sorting playing cards, low-high), an insertion sort is not efficient for large lists, but is relatively fast for adding a small number of new items periodically.

Now, here's an example of an **iterative sort function**:
```python
    def insertion_sort(list):
    # Separate the first element fom the rest of the array
    # Think about it as a sorted list of one element
    # For all other indices, beginning with [1]:
    for i in range(1, len(list)):
        # a. Copy the item at that index into a temp variable
        temp = list[i]
        # b. Iterate to the left until you find the correct index in the "sorted" list
        # part of the array at which this element should be inserted       
        j = i
        while j > 0 and temp < list[j - 1]:
            # Shift items to the right as you iterate
            list[j] = list[j - 1]
            j -= 1
        # c. When the correct index is found, copy temp into this position
        list[j] = temp
    return list
```
Here's our list:

    list = [5, 3, 1, 6]

- In this iterative sort function, the first number is already sorted (`list[0]`) 
- In this case, the sorted list is 5. 
- This is because we're looping starting from 1, because we declared it as 1
    - `for i in range(1,`...
- ending to the length of the list.
    - ...`len(list))`
- so that everything to the left of `i` is sorted.

### Iteration 1:

    list = [5, 3, 1, 6]

    i = 1  
    temp = 3 # This is the number we want to insert into the sorted half on the left
    j = 1 

1. Right now `i` is `1`.
2.  Our first operation is `temp = list[i]`. 
    - So, `temp = list[1]`, which means `temp` is now `3`.
3. The second operation assigns `j` as `i`. 
    - So `j` is now `1`.
4. The third operation is a while loop:
    - `while j > 0 and temp < list[j - 1]:`
    - this runs as long as `j` is *greater than zero* 
    - and `temp` is *smaller than list, index of `j - 1`*, which now is `list[0]`
    - so `while 1 > 0 and 3 < 5`
    - which fulfills the while condition
5. The while loop overwrites the list index of j. `list[j] = list[j - 1]`
    - so `list[1] = list[0]`, which is `5`.
    
        ```list = [5, 5, 1, 6]```
6. The fourth opertation, `j -= 1`, subtracts 1 from `j`.
    - `j` is now `0`.
    - `j` is no longer greater than `0`. Exit out of the while loop.
7. The fifth operation is `list[j] = temp`
    - It overwrites `list[j]`, which right now is `list[0]`, with `temp`.
    - `temp` is currently `3`, so it will overwrite it with 3.
    
       ```list = [3, 5, 1, 6]```

The for loop will continue until the end of the length of the list.

### Iteration 2:

    list = [1, 3, 5, 6]

    i = 2  
    temp = 1 
    j = 2 

### Iteration 3:

    list = [1, 3, 5, 6]

    i = 3 
    temp = 6 
    j = 3 


## Binary Search

Let's say you need to find a specific user from a database.

Searching through your entire database for one user is an `O(n)` function. The time complexity increases as the database of users increases. 

Now, let's look at Facebook. Searching for one user in the massive pool of Facebook's users means running a billion operations for a single retrieval. How do we optimize this?

**We optimize this by sorting. We reduce the size of the potential results using binary search.**

**Binary Search:** Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one. 










    











