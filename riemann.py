import numpy as np
import matplotlib.pyplot as plt
from .integrate import Integrate

class Riemann(Integrate):
    """
    Compute the Riemann sum of f(x) over the interval [a,b].
            
    Parameters
    ----------
    f : function
    A single variable function f(x), ex: lambda x:np.exp(x**2)
    """
    def __init__(self, f):
        Integrate.__init__(self, f)
        self.N = 25

    def compute_integral(self, a, b, N = 25, method='midpoint'):
        """
        Approximate the value of the integral of f(x) dx from a to b with N sub-intervals using left, right or midpoint method
        
        Parameters
        ----------
        a , b : any numbers
        Endpoints of the interval [a,b]
        
        N : integer
        Number of subintervals of equal length in the partition of [a,b]
        
        method : string
        Determines the kind of Riemann sum:\n
        right : Riemann sum using right endpoints\n
        left : Riemann sum using left endpoints\n
        midpoint (default) : Riemann sum using midpoints

        Returns
        -------
        float
            Approximation of the integral given by the Riemann sum.
        
        Examples
        --------
        >>> compute_integral(0,np.pi/2,1000), f = lambda x:1/(1 + x**2)
        approx = 1.3731040812301096
        actual = 1.373400766945016
        """
        self.a = a
        self.b = b
        self.N = N

        dx = (self.b - self.a) / self.N
        x = np.linspace(self.a, self.b, self.N+1)

        if method == 'left':
            x_left = x[:-1] # from 0 to N-1
            return np.sum(self.f(x_left)*dx)
        elif method == 'right':
            x_right = x[1:] # from 1 to N
            return np.sum(self.f(x_right)*dx)
        elif method == 'midpoint':
            x_mid = (x[:-1] + x[1:])/2  # all N but averaged
            return np.sum(self.f(x_mid)*dx)
        else:
            raise ValueError("Method must be 'left', 'right' or 'midpoint'.")
    
    def plot_function(self):
        
        x = np.linspace(self.a, self.b, self.N+1)
        y = self.f(x)

        X = np.linspace(self.a, self.b, 5*self.N+1)
        Y = self.f(X)

        plt.figure(figsize=(15,5))

        plt.subplot(1,3,1)
        plt.plot(X,Y,'b')
        x_left = x[:-1] # Left endpoints
        y_left = y[:-1]
        plt.plot(x_left,y_left,'b.',markersize=10)
        plt.bar(x_left, y_left,width=(self.b - self.a) / self.N, alpha=0.2, align='edge', edgecolor='b')
        plt.title('Left Riemann Sum, N = {}'.format(self.N))

        plt.subplot(1,3,2)
        plt.plot(X,Y,'b')
        x_mid = (x[:-1] + x[1:])/2 # Midpoints
        y_mid = self.f(x_mid)
        plt.plot(x_mid, y_mid, 'b.', markersize=10)
        plt.bar(x_mid, y_mid,width=(self.b - self.a) / self.N, alpha=0.2, edgecolor='b')
        plt.title('Midpoint Riemann Sum, N = {}'.format(self.N))

        plt.subplot(1, 3, 3)
        plt.plot(X, Y, 'b')
        x_right = x[1:] # Left endpoints
        y_right = y[1:]
        plt.plot(x_right, y_right,'b.', markersize=10)
        plt.bar(x_right, y_right,width=-(self.b - self.a) / self.N, alpha=0.2, align='edge', edgecolor='b')
        plt.title('Right Riemann Sum, N = {}'.format(self.N))

        plt.show()