FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN \
    apt-get -y -qq update &&\
    apt-get -y -qq dist-upgrade &&\
    apt-get install -y python-pip git &&\
    apt-get -y install \
    make build-essential libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
    xz-utils tk-dev

# pyenv settings
RUN         curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
ENV         PATH /root/.pyenv/bin:$PATH
RUN         pyenv install 3.6.3

RUN         echo 'export PATH="/root/.pyenv/bin:$PATH"' >> ~/.bashrc
RUN         echo 'eval "$(pyenv init -)"' >> ~/.bashrc
RUN         echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

# pyenv virtualenv
RUN         pyenv virtualenv 3.6.3 app

RUN         mkdir -p /app
WORKDIR     /app
COPY        .   /app
RUN         chmod +x ./docker/prod/start-prod.sh
ENTRYPOINT ["/app/docker/prod/start-prod.sh"]