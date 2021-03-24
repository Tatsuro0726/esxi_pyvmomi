FROM python:3.7-slim

RUN apt-get update &&\
    apt-get install -y git sudo wget curl &&\
    pip install --upgrade pip &&\
    pip install autopep8 flake8 pyyaml openpyxl

WORKDIR /app

# install pyvmomi 
RUN cd /app &&\
    git init &&\
    git clone https://github.com/vmware/pyvmomi.git &&\
    cd pyvmomi &&\
    python setup.py install

CMD ["/bin/bash"]