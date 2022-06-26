import unittest
from main import generate_2d_array, replace_every_max_element_with_zero, \
    insert_zero_column_after_column_with_max_element, delete_column_with_odd_positive_element, \
    replace_first_with_before_last_column


class MyTestCase(unittest.TestCase):
    def test_generating(self):
        print("Testing Generator:")
        array_empty = generate_2d_array(0, 0, -10000, 10000)
        self.assertEqual(array_empty == [], True)  # add assertion here
        array_wrong = generate_2d_array(-1, -1, -99912391239, 48523849392)
        self.assertEqual(array_wrong == [], True)  # add assertion here
        array_extremely_high_values = generate_2d_array(5, 5, -999999999999999999, 999999999999999999)
        self.assertEqual(len(array_extremely_high_values) == 5, True)  # add assertion here
        self.assertEqual(len(array_extremely_high_values[1]) == 5, True)  # add assertion here
        print(array_extremely_high_values)

        # array_extremely_large = generate_2d_array(9999999999, 999999999, -1000, 1000)
        # self.assertEqual(len(array_extremely_large) == 9999999999, True)  # add assertion here
        # self.assertEqual(len(array_extremely_large[555555]) == 9999999999, True)  # add assertion here
        # ^ рантайм падает, введу ограничение по значениям
        array_normal = generate_2d_array(15, 15, -100, 100)
        self.assertEqual(len(array_normal) == 15, True)  # add assertion here
        self.assertEqual(len(array_normal[3]) == 15, True)  # add assertion here
        print(array_normal)

    def test_replacing_max_value_with_zero(self):
        print("Testing replacing max value with zero:")
        test_array = [[-1000, 500, 1000, 5000, 1500000],
                      [-2123, 5235, 4357, 232, 1],
                      [-45753231, 543, 22323, 56734, 735674],
                      [-1, 2222, 31000, 441241, 6346575],
                      [-63465, 2323212312, 344562334, 453433243, 222222222222]]
        tested_array = replace_every_max_element_with_zero(test_array)
        print(tested_array)
        self.assertEqual(len(tested_array) == 5, True)  # add assertion here
        self.assertEqual(len(tested_array[4]) == 5, True)  # add assertion here
        self.assertEqual(tested_array[0][4] == 0, True)  # add assertion here
        self.assertEqual(tested_array[1][1] == 0, True)  # add assertion here
        self.assertEqual(tested_array[2][4] == 0, True)  # add assertion here
        self.assertEqual(tested_array[3][4] == 0, True)  # add assertion here
        self.assertEqual(tested_array[4][4] == 0, True)  # add assertion here

    def test_adding_zero_column_after_max_value_column(self):
        print("Testing column add after max value column:")
        test_array = [[0, 0, 0, 0, 1],
                      [0, 0, 0, 1, 0],
                      [0, 1, 0, 0, 0],
                      [1, 0, 0, 0, 0],
                      [1, 1, 0, 0, 1]]
        test_array2 = [[235, 12356, 23221, 53456, 122],
                       [4235, 45634, 7676, 124, 5464],
                       [145125, 32333, 19283, -1235, 3432],
                       [3887, 29393, 93939393, 124124, 544354],
                       [1, 1, 0, 0, 1]]
        tested_array = insert_zero_column_after_column_with_max_element(test_array)
        tested_array2 = insert_zero_column_after_column_with_max_element(test_array2)
        print(tested_array)
        print(tested_array2)
        self.assertEqual(len(tested_array[0]) == 9, True)
        self.assertEqual(tested_array[0][8] == 0, True)
        self.assertEqual(tested_array[3][8] == 0, True)
        self.assertEqual(len(tested_array2[0]) == 6, True)
        self.assertEqual(tested_array[0][3] == 0, True)
        self.assertEqual(tested_array[3][3] == 0, True)

    def test_delete_column_with_odd_positive_element(self):
        print("Testing odd and positive column deletion:")
        test_array = [[0, 2, 4, 6, 9],
                      [0, 2, 3, 6, 8],
                      [0, 2, 4, 6, 8],
                      [0, 2, 4, 6, 8],
                      [0, 2, 4, 6, 8],
                      [0, 1, 4, 6, 8],
                      [0, 2, 4, 6, 8]]
        test_array2 = [[15922, 54933, 2030],
                       [12222, 12, 222],
                       [3333, 2, 2]]
        tested_array = delete_column_with_odd_positive_element(test_array)
        tested_array2 = delete_column_with_odd_positive_element(test_array2)
        print(tested_array)
        print(tested_array2)
        self.assertEqual(len(tested_array[0]) == 2, True)
        self.assertEqual(tested_array[0][0] == 0, True)
        self.assertEqual(len(tested_array2[0]) == 1, True)
        self.assertEqual(tested_array2[0][0] == 2030, True)
        self.assertEqual(tested_array2[2][0] == 2, True)

    def test_replace_first_with_before_last_column(self):
        print("Testing replacing first column with before last one:")
        test_array = [[]]
        test_array2 = [[1, 2, 3], [2, 3, 4], [4, 5, 6]]
        test_array3 = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]]
        tested_array = replace_first_with_before_last_column(test_array)
        tested_array2 = replace_first_with_before_last_column(test_array2)
        tested_array3 = replace_first_with_before_last_column(test_array3)
        print('Tested Array 1: ' + str(tested_array))
        print('Tested Array 2: ' + str(tested_array2))
        print('Tested Array 3: ' + str(tested_array3))
        self.assertEqual(tested_array == [[]], True)
        self.assertEqual(tested_array2[0][1] == 1, True)
        self.assertEqual(tested_array2[1][0] == 3, True)
        self.assertEqual(tested_array3[2][0] == 6, True)
        self.assertEqual(tested_array3[2][3] == 3, True)


if __name__ == '__main__':
    unittest.main()
