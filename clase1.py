import unittest

def decimaltoRoman(decimal):
    if decimal <= 3:
        return "I" * decimal
    elif decimal == 5:
        return "V"
    elif decimal > 5 and decimal <9:
        return "V" + "I" * (decimal - 5)
    else:
        return "X"

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

if __name__ == '__main__':
    unittest.main()
