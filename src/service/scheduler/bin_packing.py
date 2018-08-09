__author__ = 'gritt'


class BinPacking:

    def __init__(self):
        pass

    def get_best_fitting_talk(self, bin_size, talks):

        # find the best fitting talk to fill the remaining bin size

        index = 0
        best_fitting_index = -1
        best_fitting_percentage = 0

        for talk in talks:

            try:
                percentage = self._calculate_fittingness(
                    bin_size,
                    talk.get_duration()
                )

                if percentage > best_fitting_percentage:
                    best_fitting_index = index
                    best_fitting_percentage = percentage

                index += 1
            except Exception:
                index += 1
                continue

        if best_fitting_index == -1:
            raise Exception("Error: neither talk fits the bin size")

        return best_fitting_index

    def _calculate_fittingness(self, bin_size, pack_size):
        if bin_size < pack_size:
            raise Exception("Error: this package is too large for this bin")

        return (pack_size * 100) / bin_size
