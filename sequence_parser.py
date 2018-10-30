import sys
import copy

class Nucleotide:
    """
    Represents one nucleotide in a sequence.
    """
    def __init__(self, modification, base, backbone, linkage=None):
        """
        :param modifications: '-' or other
        :param base: nucleotide (e.g. A,C,G,T,U)
        :param backbone: sugar e.g. one of r (RNA), d (DNA), m (modified)
        :param linkage: phosphate linkage (e.g. o or s)
        """


        self.modification = modification

        if not base in ['A', 'C', 'G', 'T', 'U']:
            sys.stderr.write("Warning: strange base detected: {}".format(base))

        self.base = base

        if not backbone in ['r', 'd', 'm']:
            sys.stderr.write("Warning: strange backbone detected: {}".format(backbone))

        self.backbone = backbone

        if linkage is not None and linkage not in ['o', 's']:
            sys.stderr.write("Warning: strange linkage {}".format(linkage))

        self.linkage = linkage

        if linkage is None:

            self.is_end = True
        else:
            self.is_end = False


    def __repr__(self):
        return ("mod:{},base:{},backbone:{},linkage:{}"
                .format(self.modification, self.base, self.backbone, "None" if self.is_end else self.linkage))


    def __str__(self):
        return self.__repr__()


class Sequence:

    def __init__(self, sequence_string):
        """
        Sanity-checks sequence to make sure it's valid, and parses into list of Nucleotide-s.
        :param sequence_string:
        """
        self.sequence_string_raw = copy.copy(sequence_string) # save this by copying; don't want to mutate accidentally


        self.sequence = [] # will hold list of Nucleotides.

        # there should be a start every 4 positions

        for nucleotide_start_idx in range(0, len(sequence_string) +1, 4):

            # populate from string

            modification = sequence_string[nucleotide_start_idx]
            base = sequence_string[nucleotide_start_idx+1]
            backbone = sequence_string[nucleotide_start_idx+2]
            try:
                linkage = sequence_string[nucleotide_start_idx+3]
            except IndexError:
                linkage = None

            # make object
            new_nuc = Nucleotide(modification=modification, base=base, backbone=backbone, linkage=linkage)

            # add to object list

            self.sequence += [new_nuc]

        # Make sure last in sequence has no linkage
        if not self.sequence[-1].is_end:
            sys.stderr.write("Warning; last nucleotide ({}) seems to have a linkage".format(self.sequence[-1]))


    def sequence_length(sequence_str):
        """
        Determines length of sequence string
        :param sequence_str:
        :return:
        """

    def __repr__(self):
        return str(list(str(base) for base in self.sequence))

    def __str__(self):
        return (self.__repr__())

