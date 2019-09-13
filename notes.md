# Iterative Sorting w/ Brady Fukumoto

## BIG-O and TIME COMPLEXITY
### How does the performance of your code scale based on the size of your inputs?
- e.g. Speed of your code with 5 users vs 5000. 

#### Big-O Cheat Sheet: [https://www.bigocheatsheet.com/]

### Performance Curve

#### 0(1):

The time complexity of this is going to be `0(1)`, which means that it is `constant`. The reason why this is constant(constant time operation) is because we're returning a pointer to the start of our list. This doesn't necessarily mean it would be faster to return a smaller list vs. a bigger list--all you're returning is one operation, which is returning the start of the list.


    animals = ['Duck', 'Jackal', 'Aardvark', 'Hippo', 'Cat', 'Flamingo', 'Iguana', 'Giraffe']


    # returns the names of all animals
    def getAnimals():
        return animals

#### 0(n)

    # returns the number of all animals
    def countAnimals():
        num_animals = 0
        for animal in animals:
            num_animals +=1
        return num_animals

    # returns 
