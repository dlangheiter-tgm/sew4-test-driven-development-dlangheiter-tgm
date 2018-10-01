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

    def testrsubError(self):
        """TypeError!!!

        self.b2=2.0-self.b2
        """
        self.assertRaises(TypeError, self.b2.__rsub__, 2.0)

    def testiSub2(self):
        self.b -= Bruch(2)
        assert(self.b == Bruch(-1, 2))

    def testrsub(self):
        self.b2 = 3 - Bruch(3, 2)
        assert(float(self.b2) == 1.5)
