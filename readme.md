# Sorting Algorithms
For the purpose of this module, we will be writing and discussing all sorting algorithms with the assumption that our goal is to sort items in ascending order. But be aware, this does not always have to be the case.

## Day 1 - Why is it so important to sort data?

### We're Always Searching
With every passing day, users have less patience for slow apps. And rightfully so! And while a large part of why the applications we use now-a-days are so fast is due to the improvements in hardware over the last few decades, the software developer still has an important role to play in keeping everything moving quickly.

As we write our applications, we should always be mindful of what operations are being done frequently, since optimizing these will have the biggest impact on the efficiency of our overall application. And regardless of *what* type of app you are creating, it is likely that one of the operations you will be relying on is ***searching***. We search [example 1], [example 2], and [example 3]. Because of this, it is essential that we optimize our searches.

### Linear vs. Binary Search
There are two common searching algorithms that developers are often introduced to when they are writing some of their first apps: linear search and binary search. Let's walk through the differences between them.

#### Linear (Sequential) Search

Sometimes referred to as sequential search, this algorithm is fairly straightforward. Given a set of data, traverse the dataset one item at a time until either you find the item you are looking for OR check every item in the set and verify the item you are looking for is not there.

#### Binary Search

The process of performing a binary search has a couple of extra steps. First, there is a *precondition* that the set of data you are searching is ***already sorted***. Then, the steps to search are:

1. Compare the item in the middle of the data set to the item we are searching for.
    - If it is the same, stop. We found it and are done!
    - Else, if the item we are searching for is LESS than the item in the middle:
        - Eliminate the RHS of list. Repeat step 1 with only the LHS of list.
    - Else: ...


A visualization comparing these two algorithms is shown below.
![binary v sequential](https://www.mathwarehouse.com/programming/images/binary-vs-linear-search/binary-and-linear-search-animations.gif "Binary v Sequential Search")

#### Runtimes

These two searching strategies have very different runtimes.

**Linear Search:** O(n)  
**Binary Search:** O(log(n))

Looking at the above runtimes, it is clear that we want to avoid linear search. 
***However, we cannot perform binary search if our data isn't ALREADY SORTED!***

While the justification for *WHY* we want to sort our data is pretty clear, a harder question to answer is *HOW* do we want to sort our data. Over the next few days, we will explore several different sorting algorithms, examining the pros and cons of each.

[(VIDEO) 15 Sorting Algorithms in 6 Minutes  ![alt text](https://i.ytimg.com/vi/kPRA0W1kECg/maxresdefault.jpg)](https://www.youtube.com/watch?v=kPRA0W1kECg)

## Iterative Sorting Algorithms

### Selection Sort
***Selection Sort*** is an algorithm that many of you have actually used before. Imagine that you have several playing cards you need to put in order. You start off by looking for the lowest card, and when you find it, put it at the front of your hand. Then, you look for the second lowest card and insert it directly behind the first card. You repeat this process, selecting the next lowest card and moving it behind the most recently placed card, until you have moved all cards into the right place. This is ***Selection Sort***.  

An example of this algorithm being applied to an array with 10 numerical elements can be seen in the video below.

[(VIDEO) Select-sort with Gypsy folk dance  ![alt text](https://i.ytimg.com/vi/Ns4TPTC8whw/hqdefault.jpg)](https://www.youtube.com/watch?v=Ns4TPTC8whw)

>CHALLENGE: Before scrolling down, try outlining the steps for this algorithm from what you observed in the video above!


#### Algorithm
1. Start with current index = 0

2. For all indices EXCEPT last:

    a. Loop through elements on right-hand-side 
    of current index and find smallest element

    b. Swap element at current index with 
    smallest element found in above loop

#### Implementation in Python
```
def selectionSort():
    // For all indices EXCEPT last:
    for i in range(0, arr.length-2):
        var cur_min_index = i;
        // 1. Loop through elements on right-hand-side 
        // of current index and find smallest element
        for j in range(i+1, arr.length-2):
            if arr[j] < arr[cur_min_index]:
                cur_min_index = j;
        // 2. Swap element at current index with 
        // smallest element found in above loop
        int temp = arr[i];
        arr[i] = arr[cur_min_index];
        arr[cur_min_index] = temp;
    // return sorted array
    return arr;

// try it out
var arr = [2,5,9,7,4,1,3,8,6];
print( "Unsorted array: " + arr);
arr = selectionSort( arr );
print( "Sorted array: " + arr);

```

#### Real-World Applications
While ***Selection Sort*** is one of the easier sorting algorithms to understand and implement, it has one major drawback - its efficiency.

Recall that the runtime complexity of an algorithm, often expressed using *Big O notation*, tells us how the amount of operations our algorithm requires will grow as the size of our input grows. ***Selection Sort*** will have a runtime of O(n²) in *all* cases, making it impractical to use with many large, real-world data sets.

#### Check for understanding
1. Is ***Selection Sort*** a comparison sorting algorithm?
    <details><summary>Answer</summary> Yes, since to <i>select</i> the desired element, we compare a current value to the rest of the "unsorted" segment of our list or array.
    </details>

2. Why do we end our loop before processing the item in the last index of an array when performing ***Selection Sort***?
    <details><summary>Answer</summary> By the nature of how this algorithm works, if all other elements have been sorted, the last element will have been moved to the correct index.

3. When using ***Selection Sort***, what is the difference between the order or arrangement of elements in *best case* versus *worst case*?
    <details><summary>Answer</summary> None, since the same number of operations will be performed <b>regardless</b> of how elements are ordered.
    </details>

4. When using ***Selection Sort***, what would be the runtime of sorting elements in the best, average, and worst cases?
    <details><summary>Answer</summary> <ul>
    <li>Best case:    O(n²)</li>
    <li>Average case: O(n²)</li>
    <li>Worst case:   O(n²)</li>
    </ul>
    </details>
5. Show how the array **[4, 8, 3, 1, 9, 6]** changes as it is being sorted using ***Selection Sort***. To do this, write out the contents of the array after each pass of the algorithm. (_hint...we should only need n-1 passes to sort the array, where n is the size_)
    <details><summary>Answer</summary> <pre><samp>[1, 8, 3, 4, 9, 6]  
   [1, 3, 8, 4, 9, 6]  
   [1, 3, 4, 8, 9, 6]  
   [1, 3, 4, 6, 9, 8]  
   [1, 3, 4, 6, 8, 9]  </samp></pre></details>

### Insertion Sort
[overview] 

[(VIDEO) Insert-sort with Romanian folk dance  ![alt text](https://i.ytimg.com/vi/ROalU379l3U/hqdefault.jpg)](https://www.youtube.com/watch?v=ROalU379l3U)

#### Algorithm
1. Separate the first element from the rest of the array. Consider it a sorted list of one element.

2. For all other indices, beginning with [1]:

    a. Copy the current item into a temp variable

    b. Iterate to the left until you find the correct index in the "sorted" part of the array at which this element should be inserted  
    - Shift items over to the right as you iterate
    
    c. When the right index is found, copy temp into this position

#### Implementation in Python
```
def insertionSort():
    // TO-DO


// try it out
var arr = [2,5,9,7,4,1,3,8,6];
print( "Unsorted array: " + arr);
arr = insertionSort( arr );
print( "Sorted array: " + arr);

```

#### Real-World Applications
While ***Insertion Sort*** is...

#### Check for understanding
1. Is ***Insertion Sort*** a comparison sorting algorithm?
    <details><summary>Answer</summary>Yes, since to find the correct index at which we "insert" the current element we are sorting, we compare it to the rest of the "sorted" segment of our list or array.
    </details>

2. Consider a scenario in which you have _____. Which sorting algorithm would you chose and WHY?

3. When using ***Insertion Sort***, what is the difference between the order or arrangement of elements in *best case* versus *worst case*?
    <details><summary>Answer</summary>When performing <i><b>Insertion Sort</b></i>, the algorithm runs more efficiently if the elements are already mostly sorted. When the original array is close to sorted order, fewer comparisons are required to sort it.  But if the array is in reverse-sorted order, the number of comparisons that need to be done increases significantly.  

    For example:  `[5, 4, 3, 2, 1]`  
    
    When inserting the 1 into the correct part of the array, we have to compare it with *every* other number. While this is not such a big deal in an array with 5 elements, it gets ***very*** costly as that array becomes bigger.
    </details>

4. When using ***Insertion Sort***, what would be the runtime of sorting elements in the best, average, and worst cases?
    <details><summary>Answer</summary>
    <ul><li>Best case:    O( )</li>
    <li>Average case: O( )</li>
    <li>Worst case:   O( )</li>
    </details>

5. Show how the array **[4, 8, 3, 1, 9, 6]** changes as it is being sorted using ***Insertion Sort***. To do this, write out the contents of the array after each pass of the algorithm. (_hint...we should only need n-1 passes to sort the array, where n is the size_)
    <details><summary>Answer</summary> <pre><samp>[4, 8, 3, 1, 9, 6] (comparison done, no swap made)
   [3, 4, 8, 1, 9, 6]
   [1, 3, 4, 8, 9, 6]
   [1, 3, 4, 8, 9, 6] (comparison done, no swap made)
   [1, 3, 4, 6, 8, 9]</samp></pre></details>

### Stretch Goals

#### There are a few "order n" sorting algorithms whose runtime will be linear, even in a worst case scenario. 
Look into Radix Sort and Count Sort.
- How are these algorithms different from other iterative sorting algorithms?
    - What are the advantages/disadvantages to this type of sorting algorithm?
- Take a look a the psuedocode for these algorithms and try implementing one or both of them in Python.

#### Some other iterative sorting algorithms include Bubble Sort and Bogo Sort.
- Summarize how they work in 2-3 sentences.
- Which algorithm has a better runtime? Explain why.


## Day 2 - A Better Way to Sort

### Divide & Conquer
>A divide-and-conquer algorithm works by recursively breaking down a problem into two or more sub-problems of the same or related type, until these become simple enough to be solved directly.  
-Wikipedia

This approach can be very useful when sorting. By breaking up our original data set into subsets and recursively sorting each subset, we can obtain significant performance gains.

### Recursion Recap
Remember that when writing a recursive algorithm, there are two pieces we have to define:
- Base case
- Recursive case

Recursive cases *must* be written in a way that will eventually allow us to reach the base case. Otherwise, infinite recursion will lead to ***STACK OVERFLOW***!

## Recursive Sorting Algorithms

### Merge Sort
[overview] 

[(VIDEO) Merge-sort with Transylvanian-saxon (German) folk dance  ![alt text](https://i.ytimg.com/vi/XaqR3G_NVoo/hqdefault.jpg)](https://www.youtube.com/watch?v=XaqR3G_NVoo)

#### Algorithm
```
TBC
```
>CHALLENGE: One implementation is shown below, but take a stab at writing the code for this yourself before scrolling down!

#### Implementation in Python
```
def mergeSort():
    //TBC

// try it out
var arr = [2,5,9,7,4,1,3,8,6];
print( "Unsorted array: " + arr);
arr = mergeSort( arr );
print( "Sorted array: " + arr);

```

#### Real-World Applications
Have you ever wondered how some of the languages you use actually implement their built-in `sort()` functions? Many of them actually utilize the ***Merge Sort*** algorithm! 

#### Check for understanding
1. TBD
    <details><summary>Answer</summary> ... </details>

2. When using ***Merge Sort***, what is the difference between the order or arrangement of elements in *best case* versus *worst case*?
    <details><summary>Answer</summary> ... </details>

3. When using ***Merge Sort***, what would be the runtime of sorting elements in the best, average, and worst cases?
    <details><summary>Answer</summary>
    <ul><li>Best case:    O(nlog(n))</li>
    <li>Average case: O(nlog(n))</li>
    <li>Worst case:   O(nlog(n))</li>
    </details>

4. Show how the array **[4, 8, 3, 1, 9, 6]** changes as it is being sorted using ***Merge Sort***. To do this, write out the contents of the array after each pass of the algorithm. (_hint...we should only need n-1 passes to sort the array, where n is the size_)
   <details><summary>Answer</summary> <pre><samp>           [4, 8, 3, 1, 9, 6]       // divide
                /            \
          [4, 8, 3]       [1, 9, 6] 
            /     \         /     \
         [4, 8]   [3]    [1, 9]   [6] 
         /    \    |     /    \    |
        [4]   [8] [3]   [1]   [9] [6]   // merge
         \    /    |     \    /    |
         [4, 8]   [3]    [1, 9]   [6]
           \      /       \       /
          [3, 4, 8]       [1, 6, 9]
              \               /
              [1, 3, 4, 6, 8, 9] </samp></pre></details>

### Quick Sort
[overview] 

[(VIDEO) Quick-sort with Hungarian folk dance  ![alt text](https://i.ytimg.com/vi/ywWBy6J5gz8/hqdefault.jpg)](https://www.youtube.com/watch?v=ywWBy6J5gz8)


#### Algorithm
```
TBC
```

#### Implementation in Python
```
def quickSort():
    // TBC


// try it out
var arr = [2,5,9,7,4,1,3,8,6];
print( "Unsorted array: " + arr);
arr = quickSort( arr );
print( "Sorted array: " + arr);

```

#### Real-World Applications
While ***Quick Sort*** has "quick" in its name, it is typically not used as frequently as Merge Sort. Although it *is* quick in a best case scenario, worst case for ***Quick Sort*** is *very* bad. Because of this, it is not often chosen for production.

#### Check for understanding
1. In ***Quick Sort***, if the leftmost element of an already sorted array is chosen as the pivot, this leads to worst case performance. Explain why.

2. Consider a scenario in which you have _____. Which recursive sorting algorithm would you chose and WHY?


3. When using ***Quick Sort***, what would be the runtime of sorting elements in the best, average, and worst cases?
    <details><summary>Answer</summary>
    <ul><li>Best case:    O(nlog(n))</li>
    <li>Average case: O(nlog(n))</li>
    <li>Worst case:   O(n²)</li>
    </details>

4. Show how the array **[4, 8, 3, 1, 9, 6]** changes as it is being sorted using ***Quick Sort***. To do this, write out the contents of the array after each pass of the algorithm. (_assume the pivot will be the middle index, mid=len of subarray / 2_)
   <details><summary>Answer</summary> <pre><samp>[1, 8, 3, 4, 9, 6]  // pivot = 1  
   // Quick Sort LHS, RHS of 1
   [1, 8, 3, 4, 9, 6]  // LHS done ✓
    ✓             
   [1, 8, 3, 4, 9, 6]  // RHS pivot = 4
    ✓                
   [1, 3, 4, 8, 9, 6]  
    ✓             
   // Quick Sort LHS, RHS of 4
   [1, 3, 4, 8, 9, 6]  // LHS done ✓
    ✓  ✓  ✓  
   [1, 3, 4, 8, 9, 6]  // RHS pivot = 9
    ✓  ✓  ✓     
   [1, 3, 4, 8, 6, 9]  
    ✓  ✓  ✓        
   // Quick Sort LHS, RHS of 9
   [1, 3, 4, 8, 6, 9]  // RHS done ✓
    ✓  ✓  ✓        ✓
   [1, 3, 4, 8, 6, 9]  // LHS pivot = 6
    ✓  ✓  ✓        ✓
   [1, 3, 4, 6, 8, 9]  
    ✓  ✓  ✓        ✓
   // Quick Sort LHS, RHS of 6
   [1, 3, 4, 6, 8, 9]  // LHS, RHS done ✓
    ✓  ✓  ✓  ✓  ✓  ✓</samp></pre></details>

### Stretch Goals

#### Tim Sort is a combination of the Merge Sort and Insertion Sort algorithms.
- What programming languages use **Tim Sort** to implement their built-in `sort()` functions?
- If an interviewer asked you to describe the **Tim Sort** algorithm in 3-4 sentences, what would you say?
- Can you implement **Tim Sort** in Python?
