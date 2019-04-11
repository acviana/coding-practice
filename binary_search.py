'''
Implements a binary search algorithm.

Taken from Chapter 2 of "Classic Computer Science Problems in Python."
'''


def binary_search(element, iterable, verbose=False):
    if iterable[0] == element:
        return True
    else:
        bottom = 0
    if iterable[-1] == element:
        return True
    else:
        top = len(iterable) - 1
    while True:
        middle = (top - bottom) // 2
        if verbose:
            print(f'Top is: {iterable[top]} (index {top})')
            print(f'Middle is: {iterable[middle]} (index {middle})')
            print(f'bottom is: {iterable[bottom]} (index {bottom})')
        if iterable[middle] == element:
            if verbose:
                print('DONE: Element found at midpoint!')
                print('\n')
            return True
        elif iterable[bottom] < element and iterable[middle] > element:
            if verbose:
                print('Element not found, moving to bottom half')
                print('---')
            top = middle
            continue
        elif iterable[middle] < element and iterable[top] > element:
            if verbose:
                print('Element not found, moving to top half')
                print('---')
            bottom = middle
            continue
        else:
            if verbose:
                print('DONE: Element not found!')
                print('\n')
            return False


if __name__ == '__main__':
    assert binary_search(0, range(1,11), verbose=True) is False
    assert binary_search(1, range(1,11), verbose=True) is True
    assert binary_search(2, range(1,11), verbose=True) is True
    assert binary_search(10, range(1,11), verbose=True) is True


    assert binary_search('b', ['a', 'b', 'c'], verbose=True) is True
    assert binary_search('d', ['a', 'b', 'c'], verbose=True) is False
