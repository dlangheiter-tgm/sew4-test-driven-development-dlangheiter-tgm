"""
Created on 27.12.2013

@author: Walter Rafeiner-Magor
"""
import unittest
from bruch.Bruch import *


class TestSubtraktion(unittest.TestCase):

    def setUp(self):
        self.b = Bruch(3, 2)
        self.b2 = Bruch(self.b)
        self.b3 = Bruch(4, 2)
        pass

    def tearDown(self):
        del self.b, self.b2, self.b3
        pass

    def testminus(self):
        self.b = self.b - Bruch(4, 5)
        assert(float(self.b) == 0.7)

    def testminus2(self):
        self.b = self.b - self.b3
        assert(float(self.b) == -0.5)

    def testminus3(self):
        self.b2 = self.b - Bruch(1)
        assert(float(self.b2) == 0.5)

    def testiSubError(self):
        self.assertRaises(TypeError, self.b.__isub__, "other")

    def testiSub(self):
        self.b -= 2
        assert(self.b == Bruch(-1, 2))


if __name__ == "__main__":
    unittest.main()