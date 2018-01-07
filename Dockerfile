FROM ubuntu:16.04

MAINTAINER Guillaume Florent version: 1.2.1

RUN apt-get update && apt-get install -y \
    swig \
    git \
    python-dev \
    python-numpy-dev \
    gfortran \
    python-mpi4py \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt
ADD https://api.github.com/repos/guillaume-florent/pyOpt/git/refs/heads/master version.json
RUN git clone --depth=1 https://github.com/guillaume-florent/pyOpt

WORKDIR /opt/pyOpt/
RUN python setup.py install

CMD ["/bin/bash"]
