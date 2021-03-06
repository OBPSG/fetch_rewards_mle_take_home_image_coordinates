# syntax=docker/dockerfile:1

FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY /src /app/src

WORKDIR /app/src

CMD ["uvicorn", "main:app", "--host=0.0.0.0"]


EXPOSE 8000