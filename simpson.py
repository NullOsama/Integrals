import numpy as np
from .integrate import Integrate

class Simpson(Integrate):
    """
    Approximate the integral of f(x) from a to b by Simpson's rule.

    Simpson's rule approximates the integral of f(x) dx by the sum:
    (dx/3) sum(f(x_{2i-2} + 4f(x_{2i-1}) + f(x_{2i})) from i = 1 to N/2 where N is the number of periods.
    dx = (b - a)/N
    x_i = a + i*dx

    Parameters
    ----------
    f : function
        A single variable function f(x), ex: lambda x:np.exp(x**2)
    """
    
    
    def __init__(self, f):
        Integrate.__init__(self, f)
        self.N = 250
        
        
    def compute_integral(self, a, b, N=250):
        """
        Parameters
        ----------
        a , b : numbers
        Interval of integration [a,b] defult to [-1,1]
        
        N : even integer
        Number of sub-intervals of [a,b]

        Returns
        -------
        float
            Approximation of the integral of f(x) from a to b using
            Simpson's rule with N subintervals of equal length.

        Examples
        --------
        >>> compute_integral(0,1,10), f = lambda x : 3*x**2
        1.0
        """
        self.a = a
        self.b = b
        self.N = N
        
        if self.N % 2 == 1:
            raise ValueError("N must be an even integer.")
        dx = (self.b - self.a) / self.N
        x = np.linspace(self.a, self.b, self.N+1)
        y = [self.f(i) for i in x]
        ans = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
        return ans