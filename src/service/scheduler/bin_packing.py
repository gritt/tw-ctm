__author__ = 'gritt'


class BinPacking:

    def __init__(self):
        pass

    def calculate_fittingness_percentage(self, bin_size, pack_size):
        if bin_size < pack_size:
            raise Exception("Error: this package is too large for this bin")

        return (pack_size * 100) / bin_size
