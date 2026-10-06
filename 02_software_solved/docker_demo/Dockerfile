FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY trajectory.py .
COPY main.py .

#copy the output folder from the container to the host machine
VOLUME /app/output

ENV MPLBACKEND=Agg
CMD ["python", "main.py"]
