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

    Parameters
    ----------
    seed : int
        Seed for the random number generator.

    Returns
    -------
    sensor_a : numpy.ndarray
    sensor_b : numpy.ndarray
    timestamps : numpy.ndarray
    """
    rng = np.random.default_rng(seed)
    n = 200
    sensor_a = rng.normal(loc=25.0, scale=3.0, size=n)
    sensor_b = rng.normal(loc=27.0, scale=4.5, size=n)
    timestamps = rng.uniform(0, 10, size=n)
    return sensor_a, sensor_b, timestamps


# Create plot_scatter(...) intent comment stays
def plot_scatter(ax: "matplotlib.axes.Axes", timestamps: np.ndarray, sensor_a: np.ndarray, sensor_b: np.ndarray) -> None:
    """Plot sensor readings as scatter points.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
    timestamps : numpy.ndarray
    sensor_a : numpy.ndarray
    sensor_b : numpy.ndarray

    Returns
    -------
    None
    """
    ax.scatter(timestamps, sensor_a, color="C0", alpha=0.7, label="Sensor A", edgecolors="none")
    ax.scatter(timestamps, sensor_b, color="C1", alpha=0.7, label="Sensor B", edgecolors="none")

    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Temperature (°C)")
    ax.legend(frameon=True)
    ax.grid(True, linestyle="--", linewidth=0.5, alpha=0.6)


def plot_histogram(ax: "matplotlib.axes.Axes", sensor_a: np.ndarray, sensor_b: np.ndarray) -> None:
    """Plot overlaid histogram of sensor readings.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
    sensor_a : numpy.ndarray
    sensor_b : numpy.ndarray

    Returns
    -------
    None
    """
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


def plot_boxplot(ax: "matplotlib.axes.Axes", sensor_a: np.ndarray, sensor_b: np.ndarray) -> None:
    """Plot side-by-side boxplot of sensor readings.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
    sensor_a : numpy.ndarray
    sensor_b : numpy.ndarray

    Returns
    -------
    None
    """
    data = [sensor_a, sensor_b]
    bplot = ax.boxplot(data, labels=["Sensor A", "Sensor B"], patch_artist=True)

    colors = ["C0", "C1"]
    for patch, color in zip(bplot["boxes"], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.6)

    ax.set_ylabel("Temperature (°C)")
    ax.grid(True, linestyle="--", linewidth=0.5, alpha=0.6)


def main(seed: int = 6012) -> None:

    """Generate plots and save them to a PNG file.

    Parameters
    ----------
    seed : int

    Returns
    -------
    None
    """
    sensor_a, sensor_b, timestamps = generate_data(seed)

    fig, axes = plt.subplots(2, 2, figsize=(10, 8))

    plot_scatter(axes[0, 0], timestamps, sensor_a, sensor_b)
    axes[0, 0].set_title("Sensor readings over time")

    plot_histogram(axes[0, 1], sensor_a, sensor_b)
    axes[0, 1].set_title("Temperature distribution")

    plot_boxplot(axes[1, 0], sensor_a, sensor_b)
    axes[1, 0].set_title("Sensor comparison (boxplot)")

    axes[1, 1].axis("off")

    fig.tight_layout()
    fig.savefig("sensor_analysis.png", dpi=150, bbox_inches="tight")

    print("Saved sensor_analysis.png")


if __name__ == "__main__":
    main()