import unittest

from common import (
    concat_first_last,
    get_all_nums,
    get_digits,
    get_line_value,
    get_line_value_02,
    lookup_nums,
)


class TestLineParsing(unittest.TestCase):

    # Tests for part 1
    def test_get_digits(self):
        line = '4xhvshhtmxx7sevenf9'
        expected = ['4', '7', '9']
        self.assertEqual(get_digits(line), expected)

    def test_concat_first_last(self):
        digits = ['4', '7', '9']
        expected = '49'
        self.assertEqual(concat_first_last(digits), expected)

    def test_get_line_value(self):
        line = '4xhvshhtmxx7sevenf9'
        expected = 49
        self.assertEqual(get_line_value(line), expected)

    # Tests for part 2
    def test_get_all_nums(self):
        # It should get both digits and words that are numbers
        line = '4xhvshhtmxx7sevenf9'
        expected = ['4', '7', 'seven', '9']
        self.assertEqual(get_all_nums(line), expected)

        # It should detect repeated numbers
        line = '4xhvsh4sevenht33mxx7sevenf9'
        expected = ['4', '4', 'seven', '3', '3', '7', 'seven', '9']
        self.assertEqual(get_all_nums(line), expected)

    def test_lookup_nums(self):
        input = ['4', '4', 'seven', '3', '3', '7', 'seven', '9']
        expected = ['4', '4', '7', '3', '3', '7', '7', '9']
        self.assertEqual(lookup_nums(input), expected)

    def test_get_line_value_02(self):
        line = '4xhvshhtmxx7sevenfseven'
        expected = 47
        self.assertEqual(get_line_value_02(line), expected)

        # This really tricky one with overlapping numbers must also pass!
        line = '9oneightgl'
        expected = 98
        self.assertEqual(get_line_value_02(line), expected)

if __name__ == '__main__':
    unittest.main()