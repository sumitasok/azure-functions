FROM python:3.7.3

RUN pip install virtualenv
RUN virtualenv venv
# https://pythonspeed.com/articles/activate-virtualenv-dockerfile/
# when this fails RUN source venv/bin/activate
RUN python3 -m virtualenv --python=/usr/bin/python3 ./venv
RUN pip install azure-storage-blob==0.37.1

# RUN pip install azure-storage-blob

WORKDIR /src