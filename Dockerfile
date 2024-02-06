FROM python:3.10

RUN mkdir /app_tm

WORKDIR /app_tm

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x docker/app.sh
