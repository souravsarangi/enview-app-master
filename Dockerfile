FROM python:3.7.2-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 1020
CMD bin/run.sh 0.0.0.0
