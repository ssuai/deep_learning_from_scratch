from unittest import TestCase

from and_gate import AND


class Test(TestCase):
    def test_and_00(self):
        y = AND(0, 0)
        self.assertEqual(y, 0)

    def test_and_01(self):
        y = AND(0, 1)
        self.assertEqual(y, 0)

    def test_and_10(self):
        y = AND(1, 0)
        self.assertEqual(y, 0)

    def test_and_11(self):
        y = AND(1, 1)
        self.assertEqual(y, 1)