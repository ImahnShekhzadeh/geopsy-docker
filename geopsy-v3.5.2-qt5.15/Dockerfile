FROM ubuntu:jammy

# Set the working directory
WORKDIR /app

COPY geopsypack-src-3.5.2.tar.gz /app/

RUN apt-get update \
 && apt-get upgrade --yes \
 && apt-get install --yes --quiet --no-install-recommends \
    build-essential \ 
    python3.11-dev \
    qtbase5-dev \
    qttools5-dev-tools \
    qtdeclarative5-dev \
    libqt5svg5-dev \
    g++ \
    gfortran \
    libfftw3-dev \
    liblapack-dev \
    zlib1g-dev \
    libopenblas-dev \
 && apt-get clean

RUN /bin/bash -c \
    cd /app/ \
 && tar -xf geopsypack-src-3.5.2.tar.gz \
 && rm geopsypack-src-3.5.2.tar.gz \
 && mkdir geopsy \
 && cd geopsypack-src-3.5.2 \
 && ./configure -prefix /home/user/geopsy/ -march native --accept-license \
 && make \
 && make install \
 && rm -rf geopsypack-src-3.5.2

ENV PATH=/home/user/geopsy/bin/:$PATH
