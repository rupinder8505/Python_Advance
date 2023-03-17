import unittest 


class TestingSum(unittest.TestCase):
    def testing_sum(self):
        self.assertEqual(sum([1,2]),3,"should be 3")

    def testing_sum_tuple(self):
        self.assertEqual(sum((1,2)),3,"should be 3")

unittest.main()