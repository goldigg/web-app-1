# Obraz bazowy
FROM python:3.8-slim-buster

WORKDIR /opt/code

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
EXPOSE 5000

CMD python3 -m flask --app /home/ec2-user/web-app-1/app-1.py run --host 0.0.0.0
