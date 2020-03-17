FROM mcr.microsoft.com/azure-functions/python:2.0-python3.6

# RUN apt-get update
# RUN apt-get install software-properties-common -y
# RUN add-apt-repository ppa:ubuntugis/ubuntugis-unstable
# RUN apt-get update
# RUN apt-get install gdal-bin -y

RUN apt-get update
RUN apt-get install gdal-bin -y
RUN apt-get install python3-gdal -y
RUN apt-get install python3-numpy -y
RUN apt-get install python-pip python3-pip -y
RUN pip3 install -U numpy
RUN pip install rasterio
RUN pip install rio-cogeo

# azure-gdal:latest

ENV AzureWebJobsScriptRoot=/home/site/wwwroot \
    AzureFunctionsJobHost__Logging__Console__IsEnabled=true

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY . /home/site/wwwroot