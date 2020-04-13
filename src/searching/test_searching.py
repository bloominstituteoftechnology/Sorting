import unittest
from searching import (
    linear_search,
    binary_search,
    binary_search_recursive,
)


class SearchingTests(unittest.TestCase):

    test_arrays = (
        lambda: [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9],
        lambda: [],
    )

    test_search_items = (
        (
            lambda: -8,
            lambda: 0,
        ),
        (
            lambda: 6,
            lambda: 0,
        ),
    )

    def index_of(self, array, value):

        r = None

        try:
            r = array.index(value)

        except ValueError:
            r = None

        return r

    def test_linear_search(self):

        for test_array in self.test_arrays:

            array = test_array()

            for test_search_item in self.test_search_items:

                search_item = test_search_item()
                self.assertEqual(
                    linear_search(array, search_item),
                    self.index_of(array, search_item),
                )

    def test_binary_search(self):

        for test_array in self.test_arrays:

            array = test_array()

            for test_search_item in self.test_search_items:

                search_item = test_search_item()
                self.assertEqual(
                    binary_search(array, search_item),
                    self.index_of(array, search_item),
                )

    def test_binary_search_recursive(self):

        for test_array in self.test_arrays:

            array = test_array()

            for test_search_item in self.test_search_items:

                search_item = test_search_item()
                self.assertEqual(
                    binary_search_recursive(array, search_item, 0, len(array) - 1),
                    self.index_of(array, search_item),
                )


if __name__ == '__main__':
    unittest.main()
