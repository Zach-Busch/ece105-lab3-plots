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
    the provided integer seed. It returns 200 timestamps uniformly
    sampled from 0 to 10 seconds and two arrays of temperature
    readings for Sensor A and Sensor B.

    Parameters
    ----------
    seed : int
        Seed for the random number generator. Use the same seed to obtain
        reproducible results.

    Returns
    -------
    timestamps : numpy.ndarray
        1-D array of length 200 with timestamps uniformly sampled from
        the interval [0, 10].

    sensor_a : numpy.ndarray
        1-D array of length 200 with readings drawn from a normal
        distribution with mean 25.0 and standard deviation 3.0.

    sensor_b : numpy.ndarray
        1-D array of length 200 with readings drawn from a normal
        distribution with mean 27.0 and standard deviation 4.5.
    """
    rng = np.random.default_rng(seed)
    n = 200
    timestamps = rng.uniform(0, 10, size=n)
    sensor_a = rng.normal(loc=25.0, scale=3.0, size=n)
    sensor_b = rng.normal(loc=27.0, scale=4.5, size=n)
    return timestamps, sensor_a, sensor_b
