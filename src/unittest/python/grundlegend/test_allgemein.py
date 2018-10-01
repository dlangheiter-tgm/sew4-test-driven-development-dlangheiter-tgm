"""
Created on 27.12.2013

@author: Walter Rafeiner-Magor <wrafeiner-magor@tgm.ac.at>
"""
import unittest
from bruch.Bruch import *


class TestAllgemein(unittest.TestCase):

    def setUp(self):
        self.b = Bruch(3, 2)
        self.b2 = Bruch(self.b)
        self.b3 = Bruch(4, 2)
        pass

    def tearDown(self):
        del self.b, self.b2, self.b3
        pass

    def testFloat(self):
        b = Bruch(3, 4)
        assert(float(b) == 0.75)

    def testInt(self):
        b = Bruch(5, 4)
        assert(int(b) == 1)

    def testComplex(self):
        b = Bruch(3, 4)
        assert(complex(b) == 0.75)

    def testInvert(self):
        z, n = 5, 4
        b = Bruch(z, n)
        assert(~b == Bruch(n, z))

    def testcreateBruchZeroError(self):
        self.assertRaises(ZeroDivisionError, Bruch, 3, 0)

    def testcreateBruchWrongTypeNenner(self):
        self.assertRaises(TypeError, Bruch, 3, 1.1)

    def testcreateBruchWrongTypeZaehler(self):
        self.assertRaises(TypeError, Bruch, 2.0)

    def testPow(self):
        h = 4
        assert(self.b2 ** h == Bruch(self.b2.zaehler ** h, self.b2.nenner ** h))

    def testPowError1(self):
        self.assertRaises(TypeError, self.b2.__pow__, 2.0)

    def testPowError2(self):
        self.assertRaises(TypeError, self.b2.__pow__, "other")

    def testAbs(self):
        b4 = Bruch(-3, 2)
        assert(abs(b4) == Bruch(3, 2))

    def testNeg(self):
        b4 = Bruch(-3, 2)
        assert(-b4 == Bruch(3, 2))

    # test of references
    def testRef(self):
        assert(self.b is not self.b2)

    def testRef2(self):
        b4 = self.b
        assert(self.b is b4)


if __name__ == "__main__":
    unittest.main()