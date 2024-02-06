FROM --platform=linux/amd64 python:3.11.2

WORKDIR /usr/src/app

RUN python3 -m pip install --upgrade pip

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app/

CMD ["python3", "app.py"]

EXPOSE 5005