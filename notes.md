# Iterative Sorting w/ Brady Fukumoto

## BIG-O and TIME COMPLEXITY
### How does the performance of your code scale based on the size of your inputs?
- e.g. Speed of your code with 5 users vs 5000. 

#### Big-O Cheat Sheet: [https://www.bigocheatsheet.com/]

### Performance Curve Shapes:

#### 0(1):

The time complexity of this is going to be `0(1)`, which means that it is `constant`. The reason why this is constant(constant time operation) is because we're returning a pointer to the start of our list. This doesn't necessarily mean it would be faster to return a smaller list vs. a bigger list--all you're returning is one operation, which is returning the start of the list, regardless of the size of the list.

    import math
    import random
    import time
    from datetime import datetime

    animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat', 'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']


    # returns the names of all animals
    def getAnimals():
        return animals

#### 0(n):

This time complexity is going to be `0(n)` because as the list gets bigger, the number of operations get bigger, which increases the time spent running the function based on the number of inputs.

To be concise: Our inputs is size `n`, and for each of these inputs, the function runs. The number of operations we need to do dependent on the number of inputs; therefore, the performance curve will be a linear shape.

    # returns the number of all animals
    def countAnimals():
        num_animals = 0
        for animal in animals:
            num_animals +=1
        return num_animals

Even if the function has multiple lines of codes run, the rule is, you always drop the constant coefficient. It just matters *how many* times the cude is run rather than the complexity of the code. (e.g. even though the function has 5 lines of code it wouldn't be `0(5n)` but still would be `0(n)` because we care about the shape of the curve and not necessarily the complexity of it.)



