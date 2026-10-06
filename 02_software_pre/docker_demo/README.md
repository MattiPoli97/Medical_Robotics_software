# Docker demo

This folder runs the same core algorithm in a container.

Build:
```bash
docker build -t medical-robotics-demo .
```

To get a quick results, run:
```bash
docker run --rm medical-robotics-demo
```

To run the container in an interactive mode and control the launch of the code, run:
```bash
docker run -it \
  -v "$(pwd)/output:/app/output" \
  --entrypoint /bin/bash \
  medical-robotics-demo
```


## venv vs Docker
- `venv` isolates Python packages but uses the host OS and host Python installation.
- Docker defines a broader execution environment from a base image and can include OS-level packages and other dependencies.

In a real robotics project, the Docker image could additionally include a specific Ubuntu release, ROS 2 distribution, OpenCV, device libraries and your application.
