import unittest
from fun_with_collections import set_member as set


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertTrue(set.in_set({3,5,8,9}, 3))   #Should run True

    def test_false(self):
        self.assertFalse(set.in_set({3,5,8,9}, 10))       #Should Run False


if __name__ == '__main__':
    unittest.main()
