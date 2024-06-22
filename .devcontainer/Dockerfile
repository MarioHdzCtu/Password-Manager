FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

RUN apt-get update && apt-get install -y \
    wget \
    gcc \
    python3-dev \
    openssl

RUN wget https://r.mariadb.com/downloads/mariadb_repo_setup

RUN echo "26e5bf36846003c4fe455713777a4e4a613da0df3b7f74b6dad1cb901f324a84  mariadb_repo_setup" \
    | sha256sum -c -

RUN chmod +x mariadb_repo_setup

RUN sudo ./mariadb_repo_setup \
   --mariadb-server-version="mariadb-10.6"

RUN apt-get update && apt-get install -y \
    libmariadb3 \
    libmariadb-dev