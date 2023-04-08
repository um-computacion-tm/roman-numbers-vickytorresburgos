import unittest
from decimaltoroman import decimaltoRoman
class TestdecimaltoRoman(unittest.TestCase):

    def test_1(self):
        resultado = decimaltoRoman(1)
        self.assertEqual(resultado,"I")

    def test_10(self):
        resultado = decimaltoRoman(10)
        self.assertEqual(resultado,"X")

    def test_5(self):
        resultado = decimaltoRoman(5)
        self.assertEqual(resultado,"V")

    def test_2(self):
        resultado = decimaltoRoman(2)
        self.assertEqual(resultado,"II")

    def test_3(self):
        resultado = decimaltoRoman(3)
        self.assertEqual(resultado, "III")

    def test_6(self):
        resultado = decimaltoRoman(6)
        self.assertEqual(resultado,"VI")

    def test_7(self):
        resultado = decimaltoRoman(7)
        self.assertEqual(resultado,"VII")

    def test_8(self):
        resultado = decimaltoRoman(8)
        self.assertEqual(resultado,"VIII")
    def test_9(self):
        resultado = decimaltoRoman(9)
        self.assertEqual(resultado,"IX")

if __name__ == '__main__':
    unittest.main()