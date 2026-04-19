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
import matplotlib.pyplot as plt


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

# Create main() that generates data, creates a 1x3 subplot figure,
# calls each plot function, adjusts layout, and saves as sensor_analysis.png
# at 150 DPI with tight bounding box.    

def main(seed: int = 6012) -> None:
    """Generate data, create a 1x3 figure with the analysis plots, and save it.

    The function generates synthetic sensor data using generate_data(),
    creates a 1x3 Matplotlib figure containing a scatter plot, a
    histogram comparing the two sensors, and a side-by-side boxplot.
    The resulting figure is saved to ``sensor_analysis.png`` at 150 DPI
    with a tight bounding box. The function modifies Matplotlib objects
    in place and returns None.

    Parameters
    ----------
    seed : int, optional
        RNG seed for reproducible data (default is 6012).

    Returns
    -------
    None
    """
    # Generate reproducible data
    sensor_a, sensor_b, timestamps = generate_data(seed)

    # Create a 1x3 subplot figure
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))

    # Left: scatter
    plot_scatter(axes[0], timestamps, sensor_a, sensor_b)
    axes[0].set_title("Sensor readings over time")

    # Middle: histogram
    ax = axes[1]
    bins = np.linspace(min(sensor_a.min(), sensor_b.min()) - 1,
                       max(sensor_a.max(), sensor_b.max()) + 1, 31)
    ax.hist(sensor_a, bins=bins, alpha=0.5, color="C0",
            label=f"Sensor A (mean={sensor_a.mean():.2f} °C)")
    ax.hist(sensor_b, bins=bins, alpha=0.5, color="C1",
            label=f"Sensor B (mean={sensor_b.mean():.2f} °C)")
    ax.axvline(sensor_a.mean(), color="C0", linestyle="--", linewidth=2)
    ax.axvline(sensor_b.mean(), color="C1", linestyle="--", linewidth=2)
    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Count")
    ax.legend(frameon=True)
    ax.grid(True, linestyle="--", linewidth=0.5, alpha=0.6)
    ax.set_title("Temperature distribution")

    # Right: boxplot
    ax = axes[2]
    data = [sensor_a, sensor_b]
    bplot = ax.boxplot(data, labels=["Sensor A", "Sensor B"], patch_artist=True)
    # Color the boxes to match the scatter/hist colors
    colors = ["C0", "C1"]
    for patch, color in zip(bplot["boxes"], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.6)
    ax.set_ylabel("Temperature (°C)")
    ax.set_title("Sensor comparison (boxplot)")
    ax.grid(True, linestyle="--", linewidth=0.5, alpha=0.6)

    # Final layout adjustments and save
    fig.tight_layout()
    fig.savefig("sensor_analysis.png", dpi=150, bbox_inches="tight")
    print("Saved sensor_analysis.png")
    return None


if __name__ == "__main__":
    main()
