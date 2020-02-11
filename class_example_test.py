
import unittest
import src.class_example as class_example

class TestMyModule(unittest.TestCase):


    def setUp(self):
        return

    def test_do_divide(self):

        first_arg = 4
        second_arg = 2

        result = class_example.do_divide(first_arg, second_arg)

        expected_result = 2

        self.assertEqual(result, expected_result)

    def test_do_divide_by_zero(self):

        first_arg = 4
        second_arg = 0

        result = class_example.do_divide(first_arg, second_arg)

        expected_result = None

        self.assertEqual(result, expected_result)
    




