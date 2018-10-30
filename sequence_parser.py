import sys
import copy
import collections

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
        Sanity-checks sequence to make sure it's valid, and tokenizes into list of Nucleotide-s.
        :param sequence_string:
        """


        self.sequence_string_raw = copy.copy(sequence_string) # save this by copying; don't want to mutate accidentally


        self.sequence = [] # will hold list of Nucleotides.

        if not len(sequence_string):
            return

        # there should be a start every 4 positions
        for nucleotide_start_idx in range(0, len(sequence_string) +1, 4):

            # populate from string

            try:
                modification = sequence_string[nucleotide_start_idx]
                base = sequence_string[nucleotide_start_idx+1]
                backbone = sequence_string[nucleotide_start_idx+2]
            except IndexError:
                sys.stderr.write("Sequence malformed; perhaps a linker was forgotten. Input: '{}'"
                                 .format(self.sequence_string_raw))
                break
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


    def length(self):
        """
        Determines length by counting tokenized string
        :return:
        """

        return len(self.sequence)


    def product_type(self):
        """
        :return: 'vanilla RNA' if only RNA backbone, 'chimera' if both DNA and RNA, 'mod RNA' if m and r in
        backbone, plus every m has an 's' linkage.
        """

        sugar_backbone_counts = collections.defaultdict(lambda: 0) # assume no counts for everything at the start

        # tabulate
        for nt in self.sequence:
            sugar_backbone_counts[nt.backbone] +=1


        # If only r, then 'vanilla RNA'
        if sugar_backbone_counts['r'] == len(self.sequence):
            return ('vanilla RNA')

        elif sugar_backbone_counts['d'] >0 and sugar_backbone_counts['r'] >0:

            if sugar_backbone_counts['m'] >0 : # don't know what to do with mod, DNA, and RNA
                sys.stderr.write("warning: sequence seems to be DNA, RNA, AND mod somehow {}"
                                 .format(self.sequence_string_raw))
                return ('unknown')

            return('chimera')

        elif sugar_backbone_counts['m'] > 0 and sugar_backbone_counts['r'] > 0:
            for nt in self.sequence:
                if nt.backbone == 'm':
                    if nt.linkage is not None and nt.linkage !='s': # must have 's' linkage if 'm' sugar
                        return ('unkonwn')

            return ('mod RNA')
            # Make sure all 'm' sugars have 's' as linkage
        else:
            sys.stderr.write("warning: weird sequence {}".format(self.sequence_string_raw))
            return ('unkonwn')




    def __len__(self):
        return(self.length())



    def __repr__(self):
        return str(list(str(base) for base in self.sequence))

    def __str__(self):
        return (self.__repr__())


def sequence_str_to_len(sequence_str):
    """
    Function a.
    Parses and santiy-checks via the Sequence class, then returns length of input string.
    """

    return Sequence(sequence_str).length()


def sequence_str_to_product_type(sequence_str):
    """
    Function b.
    Parses, returns product_type. Warnings if something's a bit unexpected.

    """
    return Sequence(sequence_str).product_type()

