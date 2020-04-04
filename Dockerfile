FROM python:3.7-alpine

COPY . /app

RUN pip install -r /app/requirements.txt

EXPOSE 9102

ENTRYPOINT ["/usr/local/bin/python", "-u", "/app/run-speedtest.py"]