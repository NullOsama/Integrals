import numpy as np
from .integrate import Integrate

class Trapezoid(Integrate):
    
    """Approximate the integral of f(x) on the interval [a,b] by the trapezoid rule.

    The trapezoid rule approximates the integral of f(x) dx from a to b by the sum:
    dx/2 * sum(f(x_{i}) + f(x_{i-1})) from i = 1 to N, where N is the number of periods.
    dx = (b - a)/N.
    x_i = a + i*dx
    
    Parameters
    ----------
    f : function
    A single variable function f(x)
    
    a , b : numbers
    Interval of integration [a,b]
    defult to [-1,1]
    
    N : integer
    Number of subintervals of [a,b]

    Returns
    -------
    float
        Approximation of the integral of f(x) from a to b using the
        trapezoid rule with N subintervals of equal lengths.

    """
    def __init__(self, f):
        Integrate.__init__(self, f)
        self.N = 250
        self.T = None
        
        
    def compute_integral(self, a, b, N=250):
        """
        Approximate the value of the integral of f(x) dx from a to b with N sub-intervals
        
        Parameters
        ----------
        a , b : numbers
        Interval of integration [a,b]\n
        defult to [-1,1]
        
        N : integer
        Number of subintervals of [a,b]
        
        Examples
        --------
        >>> compute_integral(0,5,1000), f = lambda x:1/(1 + x**2)
        approx = 1.3734007823542813
        actual = 1.373400766945016
        """
        self.a = a
        self.b = b
        self.N = N
        x = np.linspace(self.a, self.b, self.N+1) # N+1 points make N subintervals
        y = self.f(x)
        self.dx = 1.0 * (self.b - self.a) / self.N
        self.T = (self.dx / 2) * np.sum(y[1:] + y[:-1]) # T =  x_i + x_i-1 = (x_1 + x_0) + (x_2 + x_1) + (x_3 + x_2) + ... + (x_N + x_N-1)
        return self.T