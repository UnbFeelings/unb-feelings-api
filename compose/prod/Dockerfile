# Build an debian image
FROM python:3.6

# Install SO dependecies
RUN apt-get update && apt-get install -y \
    python3-dev \
    python3-pip \
    libpq-dev \
    python3-setuptools \
    gettext \
    vim \
    build-essential \
    postgresql \
    postgresql-contrib

# Install pip dependecies
RUN pip3 install --upgrade pip

# Insert Enviroment variable
ENV MODE_ENVIROMENT=production

# Create software folder
ADD . /software
WORKDIR /software
RUN pip3 install -r requirements.txt

# Run the dev script before and after any command
ENTRYPOINT ["./prod.sh"]

# Run the server
CMD ["gunicorn", "--bind 0.0.0.0:8000", "unbfeelings.wsgi"]
