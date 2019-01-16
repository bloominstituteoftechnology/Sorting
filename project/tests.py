import unittest
from searching import *
from iterative_sorting import * 
from recursive_sorting import merge_sort, merge_sort_in_place, quick_sort

class SortingTest(unittest.TestCase):

    def test_linear_search(self):
        arr1 = [-2, 7, 3, -9, 5, 1, 0, 4, -6]
        arr2 = []

        self.assertEqual(linear_search(arr1, 6), -1)
        self.assertEqual(linear_search(arr1, -6), 8)
        self.assertEqual(linear_search(arr1, 0), 6)
        self.assertEqual(linear_search(arr2, 3), -1)


    def test_binary_search(self):
        arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9] 
        arr2 = []

        self.assertEqual(binary_search(arr1, -8), 1)
        self.assertEqual(binary_search(arr1, 0), 6)
        self.assertEqual(binary_search(arr2, 6), -1)
        self.assertEqual(binary_search(arr2, 0), -1)

    
    # def test_binary_search_recursive(self):
    #     arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9] 
    #     arr2 = []

    #     self.assertEqual(binary_search_recursive(arr1, -8, 0, len(arr1)-1), 1)
    #     self.assertEqual(binary_search_recursive(arr1, 0, 0, len(arr1)-1), 6)
    #     self.assertEqual(binary_search_recursive(arr2, 6, 0, len(arr1)-1), -1)
    #     self.assertEqual(binary_search_recursive(arr2, 0, 0, len(arr1)-1), -1)


    # def test_selection(self):
    #     arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
    #     arr2 = []
    #     arr3 = [0, 1, 2, 3, 4, 5]

    #     self.assertEqual(selection_sort(arr1), [0,1,2,3,4,5,6,7,8,9])
    #     self.assertEqual(selection_sort(arr2), [])
    #     self.assertEqual(selection_sort(arr3), [0,1,2,3,4,5])


    # def test_insertion(self):
    #     arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
    #     arr2 = []
    #     arr3 = [0, 1, 2, 3, 4, 5]

    #     self.assertEqual(insertion_sort(arr1), [0,1,2,3,4,5,6,7,8,9])
    #     self.assertEqual(insertion_sort(arr2), [])
    #     self.assertEqual(insertion_sort(arr3), [0,1,2,3,4,5])


    # def test_bubble(self):
    #     arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
    #     arr2 = []
    #     arr3 = [0, 1, 2, 3, 4, 5]

    #     self.assertEqual(bubble_sort(arr1), [0,1,2,3,4,5,6,7,8,9])
    #     self.assertEqual(bubble_sort(arr2), [])
    #     self.assertEqual(bubble_sort(arr3), [0,1,2,3,4,5])


    # def test_count(self):
    #     arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
    #     arr2 = []
    #     arr3 = [1, 5, -2, 4, 3]

    #     self.assertEqual(count_sort(arr1), [0,1,2,3,4,5,6,7,8,9])
    #     self.assertEqual(count_sort(arr2), [])
    #     self.assertEqual(count_sort(arr3), "Error, negative numbers not allowed in Count Sort")


    # def test_merge(self):
    #     arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
    #     arr2 = []
    #     arr3 = [2]
    #     arr4 = [0, 1, 2, 3, 4, 5]

    #     self.assertEqual(merge_sort(arr1), [0,1,2,3,4,5,6,7,8,9])
    #     self.assertEqual(merge_sort(arr2), [])
    #     self.assertEqual(merge_sort(arr3), [2])
    #     self.assertEqual(merge_sort(arr4), [0,1,2,3,4,5])


    # def test_merge_in_place(self):
    #     arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
    #     arr2 = []
    #     arr3 = [2]
    #     arr4 = [0, 1, 2, 3, 4, 5]

    #     self.assertEqual(merge_sort_in_place(arr1, 0, len(arr1)-1), [0,1,2,3,4,5,6,7,8,9])
    #     self.assertEqual(merge_sort_in_place(arr2, 0, len(arr2)-1), [])
    #     self.assertEqual(merge_sort_in_place(arr3, 0, len(arr3)-1), [2])
    #     self.assertEqual(merge_sort_in_place(arr4, 0, len(arr4)-1), [0,1,2,3,4,5])


    # def test_quick(self):
    #     arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
    #     arr2 = []
    #     arr3 = [0, 1, 2, 3, 4, 5] 

    #     self.assertEqual(quick_sort(arr1, 0, len(arr1)-1), [0,1,2,3,4,5,6,7,8,9])
    #     self.assertEqual(quick_sort(arr2, 0, len(arr2)-1), [])
    #     self.assertEqual(quick_sort(arr3, 0, len(arr3)-1), [0,1,2,3,4,5])


if __name__ == '__main__':
    unittest.main()