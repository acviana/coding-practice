'''
A function that generates the nth Fibonacci number.
A function that generates the Fibonacci sequence through the nth term.
'''

def fibonacci_number(n):
    '''
    A naive recursive implementation that returns the nth Fibonacci
    number.
    '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_number(n - 1) + fibonacci_number(n - 2)


def test_fibonacci_number():
    assert fibonacci_number(7) == 8, fibonacci_number(8)


def fibonacci_sequence(n):
    '''
    A naive implementation that returns 1st n values in the Fibonacci
    series.
    '''
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        temp = fibonacci_sequence(n - 1)
        return temp + [temp[-1] + temp[-2]]


def test_fibonacci_sequence():
    assert fibonacci_sequence(7) == [0, 1, 1, 2, 3, 5, 8], fibonacci_sequence(7)


if __name__ == '__main__':
    # test_fibonacci_number()
    # test_fibonacci_sequence()

    # import timeit
    # for n in range(0, 51, 5):
    #     trial = timeit.timeit(f'fibonacci_sequence(n)', globals=globals())
    #     print(f'N = {n}: {trial} s')


    # import cProfile
    # cProfile.run('fibonacci_sequence(5)')
