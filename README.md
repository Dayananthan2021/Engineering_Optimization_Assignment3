# EN3330 Engineering Optimization · Assignment 3

Reproduce the Lagrangian, dual bound, extended primal objective, saddle-point slices and lower envelope for the problem of minimizing x² subject to x ≥ 1.

## Windows simulation

With Git and Python 3.11 installed, run these commands in Command Prompt:

```bat
git clone https://github.com/Dayananthan2021/Engineering_Optimization_Assignment3.git
cd Engineering_Optimization_Assignment3
build.cmd
```

The script creates a project-local environment, installs NumPy and Matplotlib, checks the sampled optima and writes five vector PDFs in figures/. A failed numerical check stops the build. Subsequent runs reuse the environment.

## Rebuilding the personal report

The separate report bundle includes report.tex, university.png and the simulation. Extract it and open Command Prompt there. Set the author in report.tex if needed. Run `build.cmd YOURINDEX` with your actual alphanumeric index. The build uses the supplied index on the cover and in the PDF filename. MiKTeX must provide pdflatex on PATH. The first build needs internet access for any missing packages.

## Other platforms

Run `python -m pip install -r requirements.txt` in a virtual environment, then `python simulate.py`. The plots use a non-interactive backend and do not require a desktop session.
