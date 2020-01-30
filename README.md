# integrals

integrals is a Python library for using numerical methods to approximate definit integrals.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install integrals.

```bash
pip install integrals
```

## Usage

```python
from integrals import Riemann, Trapezoid, Simpson
from numpy import exp

f = lambda x:exp(x**2)
riemann = Riemann(x)
print(riemann.compute_integral(-1, 3, 30, 'midpoint')) # Computing the integral of f(x) using 'Riemann midpoint sum' from -1 to 3 with 30 sub-intervals.
trapezoid = Trapezoid(f)
print(trapezoid.compute_integral(-1, 3, 30)) # Computing the integral of f(x) using 'trapezoid rule' from -1 to 3 with 30 sub-intervals.
simpson = Simpson(f)
print(simpson.compute_integral(-1, 3, 30)) # Computing the integral of f(x) using 'Simpson's rule' from -1 to 3 with 30 sub-intervals.

riemann.plot_function() # Plots the function and shows the Rieman's sum rectangles
trapezoid.plot_function() # Plots the function and shows the trapezoids
simpson.plot_function() # Plots the function and shows the sectors
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
