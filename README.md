# integrals

integrals is a Python library for using numerical methods to approximate definite integrals.

## Installation

Use the package manager <a href="https://pip.pypa.io/en/stable/" target="_blank">pip</a> to install integrals.

```bash
pip3 install integrals
```

## Usage

```python
from integrals import Riemann, Trapezoid, Simpson
from numpy import exp

f = lambda x:exp(x**2)
riemann = Riemann(f)
print(riemann.compute_integral(-1, 3, 30, 'midpoint')) # Computing the integral of f(x) using 'Riemann midpoint sum' from -1 to 3 with 30 sub-intervals.
trapezoid = Trapezoid(f)
print(trapezoid.compute_integral(-1, 3, 30)) # Computing the integral of f(x) using 'trapezoid rule' from -1 to 3 with 30 sub-intervals.
simpson = Simpson(f)
print(simpson.compute_integral(-1, 3, 30)) # Computing the integral of f(x) using 'Simpson's rule' from -1 to 3 with 30 sub-intervals.

riemann.plot_function() # Plots the function and shows the Rieman's sum rectangles
trapezoid.plot_function() # Plots the function and shows the trapezoids
simpson.plot_function() # Plots the function and shows the sectors
```
Riemann            
:-------------------------:
![Figure 1: Riemann](https://user-images.githubusercontent.com/44961698/176835779-f878e11b-b3b6-463a-93cb-e6c9ffcc9b86.png)

Trapezoid             |  Simpson
:-------------------------:|:-------------------------:
![Figure 2: Trapezoid](https://user-images.githubusercontent.com/44961698/176836121-30e25bde-c4df-43a2-881c-c0a483e166d0.png)  |  ![Figure 3: Simpson](https://user-images.githubusercontent.com/44961698/176836168-7517509e-9850-44d3-94f8-f09f60c13907.png)



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
