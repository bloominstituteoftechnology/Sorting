# Sorting Algorithms
*For the purpose of this module, we will be writing and discussing all sorting algorithms with the assumption that our goal is to sort items in ascending order. But be aware, this does not always have to be the case.*

## Tasks
 - Implement the `selection_sort` and `bubble_sort` algorithms in the `iterative_sorting` directory. 
 - Implement the `merge_sort` algorithm in the `recursive_sorting` directory. The `merge` is meant to be a helper function to the `merge_sort` function that is responsible for performing the actual merging, though you don't have to fill it out if you don't want to. 

## Stretch Goals
 - Implement all the methods in the `searching.py` file in the `searching` directory.
 - Implement the `count_sort` algorithm in the `iterative_sorting` directory.
 - Implement an in-place version of `merge_sort` that does not allocate any additional memory. In other words, the space complexity for this function should be O(1).
 - Implement the `timsort` algorithm, which is a real-world sorting algorithm. In fact, it is the sorting algorithm that is used when you run Python's built-in `sort` method. 