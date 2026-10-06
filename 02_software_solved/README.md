# Medical Robotics Software Lab — COMPLETE VERSION

## Learning path
1. Create and use a Python virtual environment (`venv`).
2. `colab/` — prototype and visualize a simple surgical-tool trajectory.
3. `vscode_demo/` — convert the notebook idea into a small Python project.
4. `docker_demo/` — run the same application inside a reproducible container.
5. `ros2_ws/` — split the application into communicating ROS 2 nodes inside a docker


## venv: QUICK START
From `vscode_demo/` folder:

macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

Windows PowerShell:
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

Exit the environment with:
```bash
deactivate
```

## Why venv is not Docker
A `venv` isolates Python packages for one project, but it still relies on the host operating system, system libraries, installed Python, and external software such as ROS.

Docker packages a broader execution environment. A container can define the base OS image, Python version, Python packages, and system-level dependencies. In robotics this is useful because a stack may depend on Ubuntu, a specific ROS distribution, OpenCV, Python libraries, and other native packages.
