# TODO 1: choose a lightweight Python 3.11 base image
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .

# TODO 2: install the Python dependencies from requirements.txt
# RUN ...

COPY trajectory.py .
COPY main.py .

VOLUME /app/output

ENV MPLBACKEND=Agg

# TODO 3: run main.py when the container starts
# CMD [...]