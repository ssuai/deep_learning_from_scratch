from unittest import TestCase, main
from ch02.nand_gate import NAND

class TestNAND(TestCase):
    def test_nand_00(self):
        self.assertEqual(NAND(0, 0), 1)

    def test_nand_01(self):
        self.assertEqual(NAND(0, 1), 1)

    def test_nand_10(self):
        self.assertEqual(NAND(1, 0), 1)

    def test_nand_11(self):
        self.assertEqual(NAND(1, 1), 0)

if __name__ == '__main__':
    main()