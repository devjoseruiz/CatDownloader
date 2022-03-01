FROM python:3.9

WORKDIR /app

COPY ./requirements.txt ./
COPY ./src ./src

RUN pip install -r requirements.txt

CMD ["python3", "./src/manage.py", "runserver", "0.0.0.0:3030"]
