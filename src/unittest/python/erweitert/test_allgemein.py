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

    def testInteger(self):
        self.b2 = Bruch(3, 1)
        assert(str(self.b2) == '(3)')

    def test_makeBruchTypeError(self):
        self.assertRaises(TypeError, Bruch._Bruch__makeBruch, "other")

    def test_makeBruchInt(self):
        value = 3
        b4 = Bruch._Bruch__makeBruch(value)
        assert(b4.zaehler == value)
