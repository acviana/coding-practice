'''
This exercise is modified from Chapter 1 of "Classic Computer Science
Problems in Python". Specifically, I used a more verbose coding style
so I could test and iterate the bit manipulation operations in
isolation that were new to me.
'''


class CompressedGene:
    '''
    Compresses a DNA sequence from a string (8-bit) to an int between 0
    and 3 (2 bits). Uses the fact that we can manipulate ints with
    bit-wise opperations.
    '''

    def __init__(self, dna_string):
        # We start with a sentinel value of 1 (`0b01`) which we have
        # remember to remove. If we started with 0 (`0b0`) we couldn't
        # shift the register e.g. `0b0 == 0b000000`
        self.bit_string = 1
        self._compress(dna_string)

    def __str__(self):
        return self.decompress()

    def _compress(self, dna_string):
        for nucleotide in dna_string.upper():
            if nucleotide == 'A':
                self._update_bit_string(0)
            elif nucleotide == 'C':
                self._update_bit_string(1)
            elif nucleotide == 'G':
                self._update_bit_string(2)
            elif nucleotide == 'T':
                self._update_bit_string(3)

    def _update_bit_string(self, interger_nucleotide_value):
        '''
        Shift the bitstring over 2 bits and then add the next
        nucleotide by using an inclusive or to flip 0's to 1's in the
        last 2 bits.
        '''
        self.bit_string = self.bit_string << 2
        self.bit_string = self.bit_string | interger_nucleotide_value

    def decompress(self):
        output = ''
        for bit in self._get_next_bit():
            if bit == 0:
                output += 'A'
            elif bit == 1:
                output += 'C'
            elif bit == 2:
                output += 'G'
            elif bit == 3:
                output += 'T'

        # Drop the sentinel and reverse the order
        return output[:-1][::-1]

    def _get_next_bit(self):
        # For n in N grab i = n * 2 bits each time.
        for i in range(0, self.bit_string.bit_length(), 2):
            this_bit = self.bit_string >> i

            # Zero out all but the last 2 bits we care about.
            yield this_bit & 0b11


def test_bit_manipulation():
    cg = CompressedGene('')
    # Note the sentinel value `0b01` is still present in each bit
    # string
    cg._update_bit_string(0)
    assert cg.bit_string == 0b100, bin(cg.bit_string)
    cg._update_bit_string(1)
    assert cg.bit_string == 0b10001, bin(cg.bit_string)
    cg._update_bit_string(2)
    assert cg.bit_string == 0b1000110, bin(cg.bit_string)
    cg._update_bit_string(3)
    assert cg.bit_string == 0b100011011, bin(cg.bit_string)


def test_compression():
    cg = CompressedGene('ACGT')
    assert cg.bit_string == 0b100011011, bin(cg.bit_string)


def test_get_next_bit():
    cg = CompressedGene('ACGT')
    bit_list = [bit for bit in cg._get_next_bit()]
    # Note the sentinel is returned
    assert [3, 2, 1, 0, 1] == bit_list, bit_list


def test_decompression():
    cg = CompressedGene('ACGT')
    assert cg.decompress() == 'ACGT', cg.decompress()


if __name__ == "__main__":
    test_bit_manipulation()
    test_compression()
    test_get_next_bit()
    test_decompression()

    from sys import getsizeof
    original: str = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
    original: str = "AAAA"
    print("original is {} bytes".format(getsizeof(original)))
    compressed: CompressedGene = CompressedGene(original) # compress
    print("compressed is {} bytes".format(getsizeof(compressed.bit_string)))
    print(compressed) # decompress
    print("original and decompressed are the same: {}".format(original == compressed.decompress()))
