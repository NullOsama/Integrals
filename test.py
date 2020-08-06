import unittest

from integrals import Trapezoid
from integrals import Simpson
from integrals import Riemann
from numpy import exp

class TestTrapezoidClass(unittest.TestCase):
    def setUp(self):
        self.trapezoid1 = Trapezoid(lambda x:1/(1+x**2))
        self.trapezoid2 = Trapezoid(lambda x:exp(x**2))
    def test_compute_integral(self):
        self.assertEqual(self.trapezoid1.compute_integral(0, 5, 10), 1.3731040812301096, 'incorrect answer')
        self.assertEqual(self.trapezoid2.compute_integral(-1, 3, 100), 1452.4837197399122, 'incorrect answer')
        self.assertEqual(self.trapezoid2.compute_integral(-1, 3, 100000), 1446.0077811218162, 'incorrect answer')
        
class TestSimpsonClass(unittest.TestCase):
    def setUp(self):
        self.simpson1 = Simpson(lambda x:1/(1+x**2))
        self.simpson2 = Simpson(lambda x:exp(x**2))
    def test_compute_integral(self):
        self.assertEqual(self.simpson1.compute_integral(0, 5, 10), 1.3714540087593017, 'incorrect answer')
        self.assertEqual(self.simpson2.compute_integral(-1, 3, 100), 1446.0365460015435, 'incorrect answer')
        self.assertEqual(self.simpson2.compute_integral(-1, 3, 100000), 1446.0077746386239, 'incorrect answer')
        
class TestRiemannClass(unittest.TestCase):
    def setUp(self):
        self.riemann1 = Riemann(lambda x:1/(1+x**2))
        self.riemann2 = Riemann(lambda x:exp(x**2))
    def test_compute_integral(self):
        self.assertEqual(self.riemann1.compute_integral(0, 5, 10), 1.373543428316664, 'incorrect answer')
        self.assertEqual(self.riemann1.compute_integral(0, 5, 10, 'left'), 1.613488696614725, 'incorrect answer')
        self.assertEqual(self.riemann1.compute_integral(0, 5, 10, 'right'), 1.1327194658454942, 'incorrect answer')
        self.assertEqual(self.riemann2.compute_integral(-1, 3, 100), 1442.7725184033638, 'incorrect answer')
        self.assertEqual(self.riemann2.compute_integral(-1, 3, 100, 'right'), 1614.4910326548509, 'incorrect answer')
        
if __name__ == '__main__':
    unittest.main()
