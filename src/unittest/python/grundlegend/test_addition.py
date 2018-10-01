"""
Created on 27.12.2013

@author: Walter Rafeiner-Magor <wrafeiner-magor@tgm.ac.at>
"""
import unittest
from bruch.Bruch import *


class TestAddition(unittest.TestCase):

    def setUp(self):
        self.b = Bruch(3, 2)
        self.b2 = Bruch(self.b)
        self.b3 = Bruch(4, 2)
        pass

    def tearDown(self):
        del self.b, self.b2, self.b3
        pass

    def testplus(self):
        self.b = self.b + Bruch(4, 5)
        assert(float(self.b) == 2.3)

    def testplus2(self):
        self.b = self.b + self.b3
        assert(float(self.b) == 3.5)

    def testplus3(self):
        self.b2 = self.b + 3
        assert(float(self.b2) == 4.5)

    def testiAdd(self):
        self.b += 1
        assert(self.b == Bruch(5, 2))

    def testiAdd2(self):
        self.b += Bruch(1)
        assert(self.b == Bruch(5, 2))

if __name__ == "__main__":
    unittest.main()