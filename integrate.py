import numpy as np
import matplotlib.pyplot as plt
class Integrate:
    
    """ base class for different numerical integration methods
    
    Parameters
    ----------
    f : function
    A single variable function f(x)
    
    a , b : numbers
    Interval of integration [a,b]
    defult to [-1,1]
    
    N : integer
    Number of subintervals of [a,b]
    """
    
    def __init__(self, f):
        self.a = -1
        self.b = 1
        self.f = f
        self.N = 100
    
    
    def plot_function(self):
        
        # x and y values for the trapezoid rule
        x = np.linspace(self.a, self.b, self.N+1)
        y = self.f(x)
        
        # X and Y values for plotting y=f(x)
        X = np.linspace(self.a, self.b, 100)
        Y = self.f(X)
        plt.plot(X,Y, c='b')
        
        for i in range(self.N):
            xs = [x[i],x[i],x[i+1],x[i+1]]
            ys = [0,y[i], y[i+1],0]
            plt.fill(xs,ys,'b',edgecolor='b',alpha=0.1)
        
        plt.title('Trapezoid Rule, N = {}'.format(self.N))
        plt.show()
            