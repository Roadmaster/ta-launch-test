FROM ubuntu:22.04

USER root

# install build dependencies and other utilities
RUN apt-get update -y && apt-get install -y \
bind9-dnsutils python3 locales hey rsync \
netcat-openbsd ncat iputils-ping mtr-tiny curl vim-tiny postgresql-client tmux \
&& apt-get clean && rm -f /var/lib/apt/lists/*_*

# Set the locale
RUN echo 'en_US.UTF-8 UTF-8' >>/etc/locale.gen && locale-gen

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# prepare build dir
WORKDIR /app
COPY header-echo.py ./

CMD ["/usr/bin/python3", "header-echo.py"]
