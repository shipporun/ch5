FROM daocloud.io/python:3.6
MAINTAINER shippo <shipporun@gmail.com>
RUN mkdir -p /app
COPY . /app
WORKDIR /app
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY docker-entrypoint.sh /user/local/bin/
RUN chmod +x /user/local/bin/docker-entrypoin.sh

EXPOSE 80
ENTRYPOINT["docker-entrypoint.sh"]
CMD[""]
