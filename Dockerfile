FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ app/
COPY tests/ tests/

# default: run the game (reads stdin, then exits)
CMD ["python", "app/treasure.py"]