import numpy as np

def plan_trajectory(start, target, n_points=50):
    """Return a straight-line 2D trajectory from start to target."""
    start = np.asarray(start, dtype=float)
    target = np.asarray(target, dtype=float)
    x = np.linspace(start[0], target[0], n_points)
    y = np.linspace(start[1], target[1], n_points)
    return np.column_stack((x, y))
