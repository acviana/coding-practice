'''
Work in progress
'''

class BinaryNumber:
    '''
    Implements binary arithmetic from scratch using strings as the
    underlaying data structure.
    '''

    def __init__(self, binary_string):
        self.value = binary_string

    def __add__(self, binary_number):
        output = ''
        column_remainder = '0'
        for a, b in zip(self.value[::-1], binary_number.value[::-1]):
            column_sum, column_remainder = self._add_binary_column(
                a, b, column_remainder
            )
            output += column_sum
        output += column_remainder
        return BinaryNumber(output[::-1])

    def __eq__(self, other_value):
        if isinstance(other_value, BinaryNumber):
            return self.value == other_value.value
        else:
            return TypeError(
                f'type {type(other_value)} is not supported for '
                f'_swap_bit ({other_value})'
            )

    def __invert__(self):
        return (
            BinaryNumber(
                ('').join([self._swap_bit(bit) for bit in self.value])
            )
        )

    def __len__(self):
        return len(self.value)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'{self.value} ({self._to_int()})'

    def __xor__(self, binary_number):
        if not isinstance(binary_number, BinaryNumber):
            raise TypeError(
                f'XOR is not defined for type {type(binary_number)}'
            )
        xor_list = [
            self._xor_bits(a, b) for a, b
            in zip(self.value, binary_number.value)
        ]
        return BinaryNumber(('').join(xor_list))

    # Class Method
    def _xor_bits(self, a, b):
        if (a, b) == ('0', '0'):
            return '0'
        elif ((a, b) == ('0', '1')) or ((a, b) == ('1', '0')):
            return '0'
        elif (a, b) == ('1', '1'):
            return '1'

    def __sub__(self, binary_number):
        if not isinstance(binary_number, BinaryNumber):
            raise TypeError(
                f'Subtraction is not defined for type {type(binary_number)}'
            )
        return self.__invert__() ^ binary_number.value

    def _to_int(self):
        return eval('0b' + self.value)
    # TODO: rewrite as class method
    def _swap_bit(self, bit):
        if bit == '0':
            return '1'
        elif bit == '1':
            return '0'
        else:
            return TypeError(
                f'type {type(bit)} is not supported for _swap_bit ({bit})'
            )

    def _add_binary_column(self, a, b, remainder='0'):
        '''
        Add a single binary column returning both the sum and the
        "remainder" to carry over to the next column.
        '''
        input = sorted((a, b, remainder))
        if input == ['0', '0', '0']:
            return ['0', '0']
        elif input == ['0', '0', '1']:
            return ['1', '0']
        elif input == ['0', '1', '1']:
            return ['0', '1']
        elif input == ['1', '1', '1']:
            return ['1', '1']
        else:
            raise TypeError(input)

    # TODO: rewrite as class method
    def _normalize(self, binary_string):
        '''
        Normalize binary strings by removing leading zeros.
        '''
        if binary_string[0] == '0':
            return self._normalize(binary_string[1:])
        else:
            return binary_string


def test_binary_number():
    # Test Normalization
    BinaryNumber('1011') == BinaryNumber('001011')

    # Test Equivalence
    eleven = BinaryNumber('1011')
    assert eleven._to_int() == 11, eleven
    thirteen = BinaryNumber('1101')
    assert thirteen._to_int() == 13, thirteen

    # Test Length
    assert len(eleven) == 4, len(eleven)
    assert len(thirteen) == 4, len(thirteen)

    #Test Addition
    assert (eleven + thirteen)._to_int() == 24, eleven + thirteen

    # Test Inversion
    assert ~eleven == BinaryNumber('0100'), ~eleven

    # Test Subtraction
    assert thirteen - eleven == 2, thirteen - eleven


if __name__ == '__main__':
    test_binary_number()
