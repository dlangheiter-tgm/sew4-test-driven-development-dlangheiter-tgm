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

    def testradd(self):
        self.b2 = 3 + Bruch(3, 2)
        assert(float(self.b2) == 4.5)

    def testaddError(self):
        self.assertRaises(TypeError, self.b2.__add__, 2.0)

    def testiAddError(self):
        self.assertRaises(TypeError, self.b.__iadd__, "other")
