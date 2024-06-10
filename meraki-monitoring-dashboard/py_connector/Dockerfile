FROM python:3.10-slim

RUN pip install influxdb_client requests pandas urllib3 meraki


COPY meraki_to_influx.py ./py_connector/
COPY config.py ./py_connector/
COPY main.py ./py_connector/
COPY influxdb_connect.py ./py_connector/

CMD ["python", "-u", "./py_connector/main.py"]
