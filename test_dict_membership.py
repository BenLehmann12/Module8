import unittest
from fun_with_collections import dict_membership as dic


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(dic.in_dict({3,6,9,12},3), True)


if __name__ == '__main__':
    unittest.main()
