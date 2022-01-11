import unittest
from unittest import TestCase
from testing.printer import Printer,PrinterError


# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)



class TestPrinter(TestCase):
    def setUp(self):
        self.printer = Printer(pages_per_s=2, capacity=300)


    def test_print_within_capacity(self):
        self.printer.print(25)


    def test_print_ouside_capacity(self):
        with self.assertRaises(PrinterError):
            self.printer.print(301)


    def test_print_exact_capacity(self):
        self.printer.print(self.printer.capacity)

    def test_printer_speed(self):
        pages = 10
        expected = 'Printer 10 pages in 5.00 seconds'
        self.assertEqual(self.printer.print(pages),expected)


    def test_always_two_decimals(self):
        fast_printer = Printer(pages_per_s=3, capacity=300)
        pages = 11
        expected = 'Printer 11 pages in 3.67 seconds'
        self.assertEqual(self.printer.print(pages), expected)

if __name__ == '__main__':
    unittest.main()
