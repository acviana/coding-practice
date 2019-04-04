'''
A function that generates the nth Fibonacci number.

A function that generates the Fibonacci sequence through the nth term.
'''

def fibonacci_number(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fibonacci_number(n - 1) + fibonacci_number(n - 2)


def test_fibonacci_number():
    assert fibonacci_number(5) == 8, fibonacci_number(5)


def fibonacci_sequence(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 2]
    else:
        temp = fibonacci_sequence(n - 1)
        return temp + [temp[-1] + temp[-2]]


def test_fibonacci_sequence():
    assert fibonacci_sequence(5) == [1, 2, 3, 5, 8], fibonacci_sequence(5)


if __name__ == '__main__':
    test_fibonacci_number()
    test_fibonacci_sequence()
