FROM python:3.12-alpine

COPY WCSeatingChartServer.py /src/server.py
COPY index.html /src/index.html

RUN pip install flask
RUN pip install flask_cors
WORKDIR /src

EXPOSE 80

CMD ["python3", "server.py"]