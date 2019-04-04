'''
Builds a calculator that reads a string and addition and subtraction.

Example:

    Input: '1+3-5+7'
    Output: 6
'''


def calculator(math_string):
    return sum([int(item) for item in math_string.replace('-', '+-').split('+')])


def test_calculator():
    assert calculator('1+3-5+7') == 6, calculator('1+3-5+7')


if __name__ == '__main__':
    test_calculator()
