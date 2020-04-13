import unittest
import random
from iterative_sorting import (
    insertion_sort,
    selection_sort,
    bubble_sort,
    count_sort,
)


class IterativeSortingTest(unittest.TestCase):

    test_arrays = (
        lambda: [1, 5, 8, 4, 2, 9, 6, 0, 3, 7],
        lambda: [],
        lambda: [2],
        lambda: [-1, 0, 1, 2, 3, 4, 5],
        lambda: random.sample(range(200), 50),
    )

    def test_insertion_sort(self):

        for test_array in self.test_arrays:

            array = test_array()
            self.assertEqual(insertion_sort(array), sorted(array))

    def test_selection_sort(self):

        for test_array in self.test_arrays:

            array = test_array()
            self.assertEqual(selection_sort(array), sorted(array))

    def test_bubble_sort(self):

        for test_array in self.test_arrays:

            array = test_array()
            self.assertEqual(bubble_sort(array), sorted(array))

    # Uncomment this test to test your count_sort implementation
    # def test_counting_sort(self):
    #
    #     for test_array in self.test_arrays:
    #
    #         array = test_array()
    #
    #         if any(item < 0 for item in array):
    #             expected_output = "Error, negative numbers not allowed in Count Sort"
    #         else:
    #             expected_output = sorted(array)
    #
    #         self.assertEqual(count_sort(array), expected_output)


if __name__ == '__main__':
    unittest.main()
