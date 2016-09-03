import unittest
from p1solution.p1solution import P1Solution


class MyTestCase(unittest.TestCase):
    EXPECTED_SUM = 233168

    def setUp(self):
        self.p1solution = P1Solution()

    def test_naive(self):
        self.assertEqual(self.p1solution.naive(), self.EXPECTED_SUM)

if __name__ == '__main__':
    unittest.main()
