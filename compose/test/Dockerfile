# Build an debian image
FROM python:3.6

# Install SO dependecies
RUN apt-get update && apt-get install -y \
    python3-dev \
    python3-pip \
    libpq-dev \
    python3-setuptools \
    gettext \
    build-essential

# Install pip dependecies
RUN pip3 install --upgrade pip

# Insert Enviroment variable
#ENV MODE_ENVIROMENT=development

# Create software folder
RUN mkdir -p /software
ADD . /software
WORKDIR /software
RUN pip3 install -r requirements.txt
