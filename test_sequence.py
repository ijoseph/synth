from unittest import TestCase
import sequence_parser

class TestSequence(TestCase):

    def setUp(self):

        self.test_vanilla = "-Uro-Uro-Aro-Gro-Cro-Uro-Aro-Aro-Cro-Gro-Gro-Uro-Ur" # length 13

        self.test_chimera = "-Uro-Uro-Aro-Gdo-Cdo-Tdo-Ado-Aro-Cro-Gro-Gro-Uro-Ur" # also 13

        self.test_mod = "-Ums-Ums-Ams-Gro-Cro-Uro-Aro-Aro-Cro-Gro-Gms-Ums-Um" # 13 again


    def test_init(self):

        self.assertIsNotNone(sequence_parser.Sequence(self.test_vanilla))
        self.assertIsNotNone(sequence_parser.Sequence(self.test_vanilla))







