import unittest
import Sort as ps


class MyTestCase(unittest.TestCase):


    def setUp(self):
        self.test_list = [10,5,4,8,1]
        pass

    def test_sort1(self):
        test_list2 = [1, 4, 5, 8, 10]
        # self.PythonSort(test_list)
        self.assertEqual(ps.insertion_sort(self.test_list), test_list2)

    def test_sort2(self):
        test_list = [12,3,5,7,-9,0]
        test_list2 = [-9,0,3,5,7,12]
        # self.PythonSort(test_list)
        self.assertEqual(ps.insertion_sort(test_list), test_list2)
    def test_sort3(self):
        test_list = [-12,-3,-5,-7,-9]
        test_list2 = [-12, -9, -7,-5,-3 ]
        # self.PythonSort(test_list)
        self.assertEqual(ps.insertion_sort(test_list), test_list2)

if __name__ == '__main__':
    unittest.main()
