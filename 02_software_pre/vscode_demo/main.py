import numpy as np
import matplotlib.pyplot as plt
from trajectory import plan_trajectory

start = np.array([0.0, 0.0])
target = np.array([0.12, 0.08])
obstacle = np.array([0.06, 0.04])
obstacle_radius = 0.02

# TODO 4: call plan_trajectory(...)
trajectory = None

fig, ax = plt.subplots(figsize=(7, 5))
# TODO 5: plot trajectory[:, 0] against trajectory[:, 1]
# ax.plot(...)
ax.scatter(*start, s=90, label="Start")
ax.scatter(*target, s=90, label="Target")
ax.add_patch(plt.Circle(obstacle, obstacle_radius, alpha=0.25, label="Anatomical structure"))
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_title("Medical Robotics Trajectory Demo")
ax.axis("equal")
ax.grid(True)
ax.legend()
plt.show()
