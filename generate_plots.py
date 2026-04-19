"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

from __future__ import annotations

import numpy as np


def generate_data(seed: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Generate simulated temperature readings from two sensors.

    The function uses a NumPy PCG64-based default_rng initialized with
    the provided integer seed. It returns two arrays of temperature
    readings for Sensor A and Sensor B and 200 timestamps uniformly
    sampled from 0 to 10 seconds.

    Parameters
    ----------
    seed : int
        Seed for the random number generator. Use the same seed to obtain
        reproducible rsesults.

    Returns
    -------
    sensor_a : numpy.ndarray
        1-D array of length 200 with readings drawn from a normal
        distribution with mean 25.0 and standard deviation 3.0.

    sensor_b : numpy.ndarray
        1-D array of length 200 with readings drawn from a normal
        distribution with mean 27.0 and standard deviation 4.5.

    timestamps : numpy.ndarray
        1-D array of length 200 with timestamps uniformly sampled from
        the interval [0, 10].
    """
    rng = np.random.default_rng(seed)
    n = 200
    sensor_a = rng.normal(loc=25.0, scale=3.0, size=n)
    sensor_b = rng.normal(loc=27.0, scale=4.5, size=n)
    timestamps = rng.uniform(0, 10, size=n)
    return sensor_a, sensor_b, timestamps

# Create plot_scatter(sensor_a, sensor_b, timestamps, ax) that draws
# the scatter plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.

def plot_scatter(ax: "matplotlib.axes.Axes", timestamps: np.ndarray, sensor_a: np.ndarray, sensor_b: np.ndarray) -> None:
    """Plot sensor readings as scatter points on an existing Axes.

    Draw Sensor A and Sensor B readings versus timestamps on the
    supplied Matplotlib Axes. The function customizes axis labels,
    a legend, and a light grid. The provided Axes is modified in
    place; the function returns None.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Matplotlib Axes object to draw into. Modified in place.

    timestamps : numpy.ndarray
        1-D array of timestamps for each reading.

    sensor_a : numpy.ndarray
        1-D array of Sensor A temperature readings.

    sensor_b : numpy.ndarray
        1-D array of Sensor B temperature readings.

    Returns
    -------
    None
    """
    # Plot each sensor with distinct colors and gentle transparency
    ax.scatter(timestamps, sensor_a, color="C0", alpha=0.7, label="Sensor A", edgecolors="none")
    ax.scatter(timestamps, sensor_b, color="C1", alpha=0.7, label="Sensor B", edgecolors="none")

    # Axis labels and legend
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Temperature (°C)")
    ax.legend(frameon=True)

    # Light dashed grid for readability
    ax.grid(True, linestyle="--", linewidth=0.5, alpha=0.6)

    # Nothing is returned; Axes modified in place
    return None
