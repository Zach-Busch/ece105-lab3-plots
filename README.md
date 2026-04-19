# Sensor Plots (ECE105 Lab 3)

Overview
--------
This repository provides a small script, `generate_plots.py`, that
produces synthetic temperature sensor data and generates publication‑quality
figures: a time-series scatter plot, an overlaid histogram comparing two
sensors, and a side-by-side boxplot. The script saves the combined figure
as `sensor_analysis.png`.

Requirements
------------
- A working Python installation (the ECE105 conda environment is recommended).
- The `ece105` conda environment (activate before installing packages).

Installation
------------
Open a terminal and run:

```bash
conda activate ece105
# then either with conda:
conda install -c conda-forge numpy matplotlib
# or with mamba (faster):
mamba install -c conda-forge numpy matplotlib
```

Usage
-----
Run the script from the repository root:

```bash
python generate_plots.py
```

The script uses a default RNG seed (6012) for reproducible synthetic data.
To change the seed, import and call the main function from Python:

```python
from generate_plots import main
main(seed=1234)
```

Output
------
- `sensor_analysis.png`: a single PNG figure (1x3 subplots) showing the
  scatter (time series), histogram (distributions), and boxplot
  comparison of the two synthetic sensors. Saved at 150 DPI with a tight
  bounding box in the repository root.

Files
-----
- `generate_plots.py` — script that generates the synthetic data and
  produces the plots.
- `sensor_analysis.png` — output image produced by the script (after
  running).
- `lab3_sensor_plots.ipynb` — original notebook used as the source for
  the script (kept for reference).

AI tools used and disclosure
---------------------------
[Placeholder] Add a short disclosure here describing any AI tools used to
assist in creating or editing this repository, including how they were
used and any limitations or verification steps performed.

License
-------
No license specified. Add a LICENSE file if one is desired.

