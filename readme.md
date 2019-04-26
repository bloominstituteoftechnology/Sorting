# Sorting Algorithms

In this two day project, you will be implementing many different solutions to the same problem: sort a list of integers in ascending order. You will also be using your newfound knowledge of complexity analysis to evaluate each implementation for efficiency.

# No Googling

Many times in your Lambda career, we encourage you to scour the internet anytime you are stumped by a problem. This is NOT one of those cases. Yes, it is possible to Google "quicksort in Python" and find a solution in about 10 seconds but that is not the point of these exercises. Your task is to take a simple problem (sort an list of ints) and a pre-defined plan (we give you an algorithm description) and turn that into code. These steps should sound familiar, as they are 1-3 of [Polya's Problem Solving techniques](https://github.com/LambdaSchool/CS-Wiki/wiki/Polya%27s-Problem-Solving-Techniques). Soon, you will be coming up with your own plans for more complex problems so don't cheat yourself out of valuable coding practice.


# Day 1

## Tasks

 - Open up the [iterative_sorting](src/iterative_sorting) directory
 - Read through the descriptions of the `bubble_sort` and `selection_sort` algorithms
 - Implement `bubble_sort` and `selection_sort` in [iterative_sorting.py](src/iterative_sorting/iterative_sorting.py)
 - Test your implementation by running `test_iterative.py`

# Day 2

## Tasks

 - Open up the [recursive_sorting](src/recursive_sorting) directory
 - Read through the descriptions of the `merge_sort` algorithm
 - Implement `merge_sort` in [recursive_sorting.py](src/recursive_sorting/recursive_sorting.py)
 - Test your implementation by running `test_recursive.py`

## Stretch Goals
 - Implement all the methods in the `searching.py` file in the `searching` directory.
 - Implement the `count_sort` algorithm in the `iterative_sorting` directory.
 - Implement an in-place version of `merge_sort` that does not allocate any additional memory. In other words, the space complexity for this function should be O(1).
 - Implement the `timsort` algorithm, which is a real-world sorting algorithm. In fact, it is the sorting algorithm that is used when you run Python's built-in `sort` method. 
