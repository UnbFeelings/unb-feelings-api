# Imagem de build do S.O debian
FROM debian:8.7

# Melhora a acessibilidade ao container
ENV PYTHONUNBUFFERED 1

# Setar o diretorio de trabalho /software dentro do container
RUN mkdir /software
ADD . /software
WORKDIR /software

# Atualizar o container
RUN apt-get update

# Instalar o S.O e suas dependencias
RUN apt-get install -y python3-dev \
    python3-pip \
    libpq-dev \
    vim \
    build-essential \
    postgresql \
    postgresql-contrib

# Instalar dependências do PIP
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
