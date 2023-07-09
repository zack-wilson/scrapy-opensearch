FROM python:slim AS base

ARG USERNAME=scrapy
ARG UUID=1000
ARG GUID=${UUID}

RUN apt-get update -y \
    && apt-get install -y \
    git sudo jq python3-pdm python3-pytest python3-pytest-cov python3-mypy python3-ipython \
    && addgroup --gid=${GUID} ${USERNAME} \
    && adduser --disabled-password --gecos "" --gid=${GUID} --uid=${UUID} ${USERNAME} \
    && echo "${USERNAME}    ALL=(root)   NOPASSWD:ALL" >/etc/sudoers.d/${USERNAME} \
    && echo 'export PATH=$HOME/.local/bin:$PATH' >> /home/${USERNAME}/.profile