"""
Created on 27.12.2013

@author: Walter Rafeiner-Magor <wrafeiner-magor@tgm.ac.at>
"""
import unittest
from bruch.Bruch import *


class TestDivision(unittest.TestCase):

    def setUp(self):
        self.b = Bruch(3, 2)
        self.b2 = Bruch(self.b)
        self.b3 = Bruch(4, 2)
        pass

    def tearDown(self):
        del self.b, self.b2, self.b3
        pass

    def testrdivError(self):
        self.assertRaises(TypeError, self.b2.__rtruediv__, 3.0)

    def testrdiv(self):
        self.b2 = 2 / Bruch(2)
        assert(float(self.b2) == 1)
