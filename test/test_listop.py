import unittest
from ut import listop

class TestListop(unittest.TestCase):

    def test_sum(self):
        testC = listop.C([1,2,3,4])
        testResult = testC.sum()
        self.assertEqual(testResult, 10)

    def test_len(self):
        testC = listop.C([1, 2, 3, 4])
        testResult = testC.len()
        self.assertEqual(testResult, 4)

    def test_sort(self):
        testC = listop.C([7,3,10,2])
        expectedResult = [2, 3, 7, 10]
        testResult = testC.sort()
        self.assertEqual(testResult, expectedResult)

    def test_append(self):
        testC = listop.C ([1,2])
        testC.append([7, 6, 5])
        expectedResult = [1, 2, 5, 6, 7]
        testResult = testC.sort()
        self.assertEqual(testResult, expectedResult)

if __name__ == '__main__':
    unittest.main()
