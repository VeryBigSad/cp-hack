FROM python:3.11.5-slim-bookworm

WORKDIR /app
ENV PYTHONUNBUFFERED=1
COPY requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY main.py main.py

ENTRYPOINT ["streamlit", "run", "main.py"]
