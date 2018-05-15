# https://github.com/tiangolo/uwsgi-nginx-docker/tree/master/python3.6
FROM tiangolo/uwsgi-nginx:python3.6
LABEL maintainer=""

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:src/"
ENV LISTEN_PORT 8000
EXPOSE 8000
ENV UWSGI_INI /opt/app/deployment/uwsgi.ini

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb http://dl.yarnpkg.com/debian/ stable main" > /etc/apt/sources.list.d/yarn.list
RUN apt-get update && apt-get install -y sudo libpcre3-dev curl gcc make git nodejs yarn

WORKDIR /opt/app/

COPY py-requirements /opt/app/py-requirements
RUN pip install pip -U && \
   pip install -r py-requirements/base.txt

ADD . /opt/app/
RUN set -x && yarn install
RUN set -x && yarn run prod

COPY init.sh /init.sh
RUN chmod +x /init.sh
ENTRYPOINT ["/init.sh"]
