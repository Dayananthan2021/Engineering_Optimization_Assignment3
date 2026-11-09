# EN3330 Engineering Optimization — Assignment 3

Generate the plots for minimizing x² subject to x ≥ 1. The simulation also checks the dual bounds for multipliers 0, 1, 2 and 3.

## Run on Windows

With Python 3.11 installed, open a terminal in the repository folder and run:

```powershell
py -3.11 -m pip install -r requirements.txt
py -3.11 simulate.py
```

The script prints the numerical checks and saves five PDF plots in `figures/`: the Lagrangian curves, dual function, primal function, saddle-point slices and lower envelope.
