import unittest

def decimaltoRoman(decimal):
    if decimal <= 3:
        return "I" * decimal
    elif decimal == 5:
        return "V"
    elif decimal > 5 and decimal <9:
        return "V" + "I" * (decimal - 5)
    elif decimal == 9:
        return "IX"
    else:
        return "X"

