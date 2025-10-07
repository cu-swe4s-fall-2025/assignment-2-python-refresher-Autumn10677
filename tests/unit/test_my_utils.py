import sys
import unittest
import random

sys.path.append("src/")  # noqa

import my_utils  # noqa


class TestMyUtils(unittest.TestCase):

    # Tests some simple examples for mean()
    def test_mean(self):
        self.assertEqual(my_utils.mean([-1, -2, 0]), -1)
        self.assertEqual(my_utils.mean([1, 2, 3, 4]), 2.5)
        self.assertEqual(my_utils.mean([1, 2, 3, 4, 5]), 3)

        with self.assertRaises(ValueError):
            my_utils.mean([])

    # Checks a random example for mean()
    def test_mean_random(self):
        data = random.sample(range(-100, 100), 100)
        self.assertEqual(my_utils.mean(data), sum(data) / len(data))

    # Tests some simple examples for median()
    def test_median(self):
        self.assertEqual(my_utils.median([-3, -10, 3]), -3)
        self.assertEqual(my_utils.median([1, 2, 3, 4]), 2.5)
        self.assertEqual(my_utils.median([5, 1, 3, 6, 8]), 5)

        with self.assertRaises(ValueError):
            my_utils.median([])

    # Checks a random example for median()
    def test_median_random(self):
        data = random.sample(range(-100, 100), 101)
        self.assertEqual(my_utils.median(data), sorted(data)[len(data) // 2])

    # Tests some simple examples for standard_deviation()
    def test_standard_deviation(self):
        self.assertAlmostEqual(
            my_utils.standard_deviation([1, 2, 3, 4, 5]), 1.4142135623730951
        )
        self.assertAlmostEqual(
            my_utils.standard_deviation([-10, 0, 1, -3]), 4.301162633521313
        )
        self.assertEqual(my_utils.standard_deviation([5]), 0)

        with self.assertRaises(ValueError):
            my_utils.standard_deviation([])

    # Checks a random example for standard_deviation()
    def test_standard_deviation_random(self):
        data = random.sample(range(-100, 100), 100)
        mean = sum(data) / len(data)
        variance = sum((x - mean) ** 2 for x in data) / len(data)
        self.assertAlmostEqual(
            my_utils.standard_deviation(data), variance**0.5
        )  # noqa: E501


if __name__ == "__main__":
    unittest.main()
