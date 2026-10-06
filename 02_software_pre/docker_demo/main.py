import os
import matplotlib.pyplot as plt
import numpy as np
from trajectory import plan_trajectory

os.makedirs("/app/output", exist_ok=True)

start = np.array([0.0, 0.0])
target = np.array([0.12, 0.08])
obstacle = np.array([0.06, 0.04])
obstacle_radius = 0.02

# TODO 4: generate the trajectory using the plan_trajectory function
trajectory = None
# TODO 5: compute Euclidean distance between start and target
distance = None

# TODO 6: plot the trajectory and save it to /app/output/trajectory.png

fig, ax = plt.subplots(figsize=(7, 5))

# TODO 7: plot the trajectory with ax.plot of the x and y coordinates of the robot trajectory
ax.plot(
    None,
    None,
    linewidth=2,
    label="Robot trajectory"
)

# TODO 8: plot the start and target positions
ax.scatter(
    None,
    None,
    s=100,
    label="Start"
)

ax.scatter(
    None,
    None,
    s=100,
    label="Target"
)

# TODO 9: plot the obstacle as a circle using ax.add_patch
obstacle_circle = plt.Circle(
    None,
    None,
    alpha=0.3,
    label="Anatomical structure"
)

ax.add_patch(obstacle_circle)

ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_title("Surgical Tool Trajectory")

ax.axis("equal")
ax.grid(True)
ax.legend()


output_file = "/app/output/trajectory.png"
# TODO 10: save the figure to the output file with plt.savefig
plt.savefig(
    None,
    dpi=200,
    bbox_inches="tight"
)

plt.close()

print(f"Trajectory plot saved to: {output_file}")
print(f"Start: {start}")
print(f"Target: {target}")
print(f"Trajectory points: {len(trajectory)}")
print(f"Straight-line distance: {distance:.3f} m")
print("Container executed successfully.")
