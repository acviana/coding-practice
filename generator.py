'''
Define a class with a generator which can iterate the numbers, which
are divisible by 7, between a given range 0 and n.

https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt#L545
'''

### WITH A GENERATOR


def divisible_by_seven(max_value):
    current_value = 1
    while current_value <= max_value:
        if current_value % 7 == 0:
            yield current_value
        current_value += 1


def test_divisible_by_seven():
    assert [item for item in divisible_by_seven(21)] == [7, 14, 21]


test_divisible_by_seven()

### WITH AN ITERATOR


class GeneratorClass:

    def __init__(self, max_value):
        self.max_value = max_value

    def __iter__(self):
        self.current_value = 7
        return self

    def __next__(self):
        if self.current_value <= self.max_value:
            temp = self.current_value
            self.current_value += 7
            return temp
        else:
            raise StopIteration


def test_generator_class():
    gc = GeneratorClass(21)
    test_list = [item for item in gc]
    assert test_list == [7, 14, 21], test_list


test_generator_class()
