# VS Code + venv

## 1. Open this folder in VS Code
Use **File → Open Folder** and select `vscode_demo`.

## 2. Create an isolated Python environment
macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

## 3. Install dependencies
```bash
pip install -r requirements.txt
```

## 4. Run
```bash
python main.py
```

## 5. Leave the environment
```bash
deactivate
```

### What did venv solve?
It isolated this project's Python packages from other projects. It did not package your operating system, ROS installation, or native system libraries. That broader reproducibility problem motivates Docker.
