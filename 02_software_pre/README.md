# Medical Robotics Software Lab — PRE VERSION

This is the hands-on version. Some lines have been intentionally removed and marked with `TODO`.

## Your mission
Work through the same application in progressively more realistic environments:
1. Create a Python virtual environment (`venv`) and install dependencies.
2. `colab/` — complete the trajectory calculation.
3. `vscode_demo/` — complete and run the modular Python project.
4. `docker_demo/` — complete the Docker recipe and run the project in a container.
5. `ros2_ws/` — complete the ROS 2 publisher/subscriber nodes.

## Virtual Environment - quick start
From `vscode_demo/`:

macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Windows PowerShell:
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

When finished:
```bash
deactivate
```

A `venv` isolates Python packages. It does **not** package the operating system, ROS installation, or system libraries. Docker addresses a larger reproducibility problem by defining the application environment around the code.
