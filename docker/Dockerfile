FROM python:3

RUN apt-get update && apt-get install -y netcat

WORKDIR .

COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY ./docker/python_start /python_start

RUN chmod +x /python_start
