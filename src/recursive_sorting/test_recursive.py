import unittest
import random
from recursive_sorting import (
    merge_sort,
    merge_sort_in_place,
)


class RecursiveSortingTests(unittest.TestCase):

    test_arrays = (
        lambda: [1, 5, 8, 4, 2, 9, 6, 0, 3, 7],
        lambda: [],
        lambda: [2],
        lambda: [-1, 0, 1, 2, 3, 4, 5],
        lambda: random.sample(range(200), 50),
    )

    def test_merge_sort(self):

        for test_array in self.test_arrays:

            arrayA = test_array()
            arrayB = test_array()
            self.assertEqual(merge_sort(arrayA), sorted(arrayB))

    # Uncomment this test to test your in-place merge sort
    # def test_in_place_merge_sort(self):
    #
    #     for test_array in self.test_arrays:
    #
    #         arrayA = test_array()
    #         arrayB = test_array()
    #         self.assertEqual(
    #             merge_sort_in_place(arrayA, 0, len(arrayA) - 1),
    #             sorted(arrayB),
    #         )


if __name__ == '__main__':
    unittest.main()
