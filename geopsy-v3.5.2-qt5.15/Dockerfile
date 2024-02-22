FROM ubuntu:jammy

# Install `conda` (not present in CUDA image)
# Use of miniconda since full anaconda distribution not needed
ENV MINICONDA_VERSION Miniconda3-latest-Linux-x86_64.sh
ENV MINICONDA_SHA_256 \
43651393236cb8bb4219dcd429b3803a60f318e5507d8d84ca00dafa0c69f1bb

RUN apt-get update && apt-get install -y curl && \
curl -O https://repo.anaconda.com/miniconda/$MINICONDA_VERSION && \
/bin/bash $MINICONDA_VERSION -b -p /opt/conda && \
rm $MINICONDA_VERSION && \
apt-get clean

# Add `conda` to path; initialize `conda`, install specific python version, 
# update `conda` and install `pip` via `conda`
ENV PATH /opt/conda/bin:$PATH
RUN conda init bash && \
conda install -y python=3.10.3 && \
conda update -n base -c defaults conda && \
conda install -c conda-forge pip && \
pip install --upgrade pip && \
pip install numpy

# Set the working directory
WORKDIR /app

COPY geopsypack-src-3.5.2.tar.gz /app/

RUN apt-get update \
 && apt-get upgrade --yes \
 && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
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
 && ./configure -prefix /home/user/geopsy/ -march native -I /opt/conda/lib/python3.10 --accept-license \
 && make \
 && make install \
 && rm -rf geopsypack-src-3.5.2

ENV PATH=/home/user/geopsy/bin/:$PATH

# Copy shell script that will be executed when the container starts
COPY run_scripts.sh .

# Ensure `run_scripts.sh` is executable
RUN chmod +x ./run_scripts.sh

# Execute `run_scripts.sh` as the entrypoint
ENTRYPOINT ["./run_scripts.sh"]