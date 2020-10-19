import unittest
from fun_with_collections import half_birthday as birthday


class MyTestCase(unittest.TestCase):
    def test_brithday(self):
        self.assertEqual(birthday.half_birthday(birthday.datetime(2019,6,18)), birthday.half_birthday(birthday.datetime(2019,6,18)))


if __name__ == '__main__':
    unittest.main()
