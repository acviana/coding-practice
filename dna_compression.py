class CompressedGene:
    '''
    Compresses a DNA sequence from a string (8-bit) to an int between 0
    and 3 (2 bits). Uses the fact that we can manipulate ints with
    bit-wise opperations.
    '''

    def __init__(self, dna_string):
        self._compress(dna_string)
        self.bit_string = 0

    def _compress(self, dna_string):
        for nucleotide in dna_string.upper():
            if nucleotide == 'A':
                print(nucleotide, 0)
            elif nucleotide == 'C':
                print(nucleotide, 1)
            elif nucleotide == 'G':
                print(nucleotide, 2)
            elif nucleotide == 'T':
                print(nucleotide, 3)

    def _update_bit_string(self, value):
        self.bit_string = self.bit_string << 2 # Add 2 zeros to the bit string.
        self.bit_string = self.bit_string + value

    def decompress(self):
        pass


def test_bit_manipulation():
    cg = CompressedGene('derp')
    cg._update_bit_string(0)
    assert cg.bit_string == 0b00, bin(cg.bit_string)
    cg._update_bit_string(1)
    assert cg.bit_string == 0b0001, bin(cg.bit_string)
    cg._update_bit_string(2)
    assert cg.bit_string == 0b000111, bin(cg.bit_string)


if __name__ == "__main__":
    test_bit_manipulation()

    # from sys import getsizeof
    # original: str = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
    # print("original is {} bytes".format(getsizeof(original)))
    # compressed: CompressedGene = CompressedGene(original) # compress print("compressed is {} bytes".format(getsizeof(compressed.bit_string))) print(compressed) # decompress
    # print("original and decompressed are the same: {}".format(original ==
    # compressed.decompress()))
