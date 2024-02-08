FROM python:latest

WORKDIR /app

COPY requirements.txt /app/
RUN  pip install -r /app/requirements.txt
ENV PYTHONUNBUFFERED 1

COPY . /app/

CMD python3 /app/app.py