import unittest
from fun_with_collections import assign_average as average


class MyTestCase(unittest.TestCase):
    def test_a(self):
        self.assertEqual(average.switch_average('A'), 100)

    def test_b(self):
        self.assertEqual(average.switch_average('B'), 80)

    def test_c(self):
        self.assertEqual(average.switch_average('C'), 70)

    def test_d(self):
        self.assertEqual(average.switch_average('D'), 60)





if __name__ == '__main__':
    unittest.main()
