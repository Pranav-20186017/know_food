FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pip3 install -r requirements.txt
RUN pip3 --no-cache-dir install --upgrade awscli
EXPOSE 8000
