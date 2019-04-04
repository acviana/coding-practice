'''
Write a program to compute the frequency of the words from the input.
The output should output after sorting the key alphanumerically.

Suppose the following input is supplied to the program:

"New to Python or choosing between Python 2 and Python 3? Read Python 2
or Python 3."

Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1

https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt#L618
'''
from collections import defaultdict


def word_frequency(input_text):
    word_counter = defaultdict(int)
    for item in input_text.split(' '):
        word_counter[item] += 1
    for key in sorted(word_counter.keys()):
        print(f'{key}:{word_counter[key]}')


def test_word_frequency():
    input_text = (
        'New to Python or choosing between Python 2 and Python 3? Read '
        'Python 2 or Python 3.'
    )
    word_frequency(input_text)


if __name__ == '__main__':
    test_word_frequency()
