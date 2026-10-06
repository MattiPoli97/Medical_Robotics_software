import numpy as np
import matplotlib.pyplot as plt

from trajectory import plan_trajectory

import os

os.makedirs("/app/output", exist_ok=True)

# -----------------------------
# 1. Define the scenario
# -----------------------------

start = np.array([0.0, 0.0])
target = np.array([0.12, 0.08])

# Example anatomical structure to avoid
obstacle = np.array([0.06, 0.04])
obstacle_radius = 0.02


# -----------------------------
# 2. Compute trajectory
# -----------------------------

trajectory = plan_trajectory(
    start,
    target,
    n_points=50
)

distance = np.linalg.norm(target - start)

# -----------------------------
# 3. Visualize trajectory
# -----------------------------

fig, ax = plt.subplots(figsize=(7, 5))

# Robot trajectory
ax.plot(
    trajectory[:, 0],
    trajectory[:, 1],
    linewidth=2,
    label="Robot trajectory"
)

# Start and target
ax.scatter(
    start[0],
    start[1],
    s=100,
    label="Start"
)

ax.scatter(
    target[0],
    target[1],
    s=100,
    label="Target"
)

# Anatomical structure
obstacle_circle = plt.Circle(
    obstacle,
    obstacle_radius,
    alpha=0.3,
    label="Anatomical structure"
)

ax.add_patch(obstacle_circle)


# -----------------------------
# 4. Configure plot
# -----------------------------

ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_title("Surgical Tool Trajectory")

ax.axis("equal")
ax.grid(True)
ax.legend()


# -----------------------------
# 5. Save result
# -----------------------------

output_file = "/app/output/trajectory.png"

plt.savefig(
    output_file,
    dpi=200,
    bbox_inches="tight"
)

plt.close()

print(f"Trajectory computed successfully.")
print(f"Start:  {start}")
print(f"Target: {target}")
print(f"Figure saved as: {output_file}")

print(f"Trajectory points: {len(trajectory)}")
print(f"Straight-line distance: {distance:.3f} m")
print("Container executed successfully.")

