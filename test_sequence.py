from unittest import TestCase
import sequence_parser

class TestSequence(TestCase):

    def setUp(self):

        self.test_vanilla = "-Uro-Uro-Aro-Gro-Cro-Uro-Aro-Aro-Cro-Gro-Gro-Uro-Ur" # length 13

        self.test_chimera = "-Uro-Uro-Aro-Gdo-Cdo-Tdo-Ado-Aro-Cro-Gro-Gro-Uro-Ur" # also 13

        self.test_mod = "-Ums-Ums-Ams-Gro-Cro-Uro-Aro-Aro-Cro-Gro-Gms-Ums-Um" # 13 again

        self.test_len_one = "-Um"

        self.test_no_linker= "-Um-Um"


    def test_init(self):

        self.assertIsNotNone(sequence_parser.Sequence(self.test_vanilla))
        self.assertIsNotNone(sequence_parser.Sequence(self.test_chimera))
        self.assertIsNotNone(sequence_parser.Sequence(self.test_mod))

        sequence_parser.Sequence(self.test_no_linker)


    def test_length(self):
        self.assertEquals(sequence_parser.Sequence(self.test_vanilla).length(), 13)
        self.assertEquals(sequence_parser.Sequence(self.test_chimera).length(), 13)
        self.assertEquals(sequence_parser.Sequence(self.test_mod).length(), 13)

        self.assertEquals(sequence_parser.Sequence(self.test_len_one).length(), 1)

        self.assertEquals(sequence_parser.Sequence("").length(), 0)


    def test_product_type(self):
        self.assertEquals(sequence_parser.Sequence(self.test_vanilla).product_type(), 'vanilla RNA')

        self.assertEquals(sequence_parser.Sequence(self.test_chimera).product_type(), 'chimera')

        self.assertEquals(sequence_parser.Sequence(self.test_mod).product_type(), 'mod RNA')
















