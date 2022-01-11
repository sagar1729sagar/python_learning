import unittest
from unittest import TestCase
from testing.functions import divide,multiply


class TestFunctions(TestCase):
    def test_divide_result(self):
        dividend = 15
        divisor = 3
        expected_result = 5.0
        self.assertAlmostEqual(divide(dividend, divisor), expected_result, delta=0.0001)

    def test_divide_negative(self):
        dividend = 15
        divisor = -3
        expected_result = -5.0
        self.assertAlmostEqual(divide(dividend, divisor), expected_result, delta=0.0001)

    def test_dividend_zero(self):
        dividend = 0
        divisor = -5
        expected_result = 0.0
        self.assertEqual(divide(dividend, divisor), expected_result)

    def test_divide_error_on_zero(self):
        self.assertRaises(ValueError,lambda : divide(25,0))
        # with self.assertRaises(ValueError):,
        #     divide(25,0)


    def test_multiply_empty(self):
        with self.assertRaises(ValueError):
            multiply()

    def test_multiply_single_value(self):
        expected = 15
        self.assertEqual(multiply(expected), expected)

    def test_multiply_zer0(self):
        expected = 0
        self.assertEqual(multiply(expected),expected)

    def test_mutiply_result(self):
        inputs=(5,3)
        expected = 15
        self.assertEqual(multiply(*inputs), expected)

    def test_multiply_result_with_zero(self):
        inputs = (5, 3, 0, 63)
        expected = 0
        self.assertEqual(multiply(*inputs), expected)

    def test_mutiply_negative_result(self):
        inputs=(5,-3)
        expected = -15
        self.assertEqual(multiply(*inputs), expected)

    def test_mutiply_floats(self):
        inputs=(5.0,3)
        expected = 15.0
        self.assertEqual(multiply(*inputs), expected)




# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)
#
#
if __name__ == '__main__':
    unittest.main()
