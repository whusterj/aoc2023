filename = "input.txt"

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
number_strs = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
number_lookup = {
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

# Functions for part 1 of the puzzle
def get_digits(line: str) -> list[str]:
    return [char for char in line if char.isdigit()]

def concat_first_last(digits: list[str]) -> str:
    return digits[0] + digits[-1]

def get_line_value(line: str) -> int:
    return int(concat_first_last(get_digits(line)))

# Additional functions for part 2 of the puzzle
def get_all_nums(line: str, acc=None) -> list[str]:
    """Recursively check the first value of the line to see if it's a match."""
    if acc is None:
        acc = []

    if not line:
        return acc

    if line[0].isdigit():
        return get_all_nums(line[1:], [*acc, line[0]])

    # This loop is inefficient - regex may be faster?
    # Doing the number lookup here would also save a loop later
    for number_str in number_strs:
        if line.startswith(number_str):
            return get_all_nums(line[1:], [*acc, number_str])

    return get_all_nums(line[1:], acc)

def lookup_nums(nums: list[str]) -> list[str]:
    return [number_lookup[x] for x in nums]

def get_line_value_02(line: str) -> int:
    return int(concat_first_last(lookup_nums(get_all_nums(line))))
