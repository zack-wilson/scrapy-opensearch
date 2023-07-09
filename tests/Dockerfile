#syntax=docker/dockerfile:1
FROM python:slim AS base

ARG USERNAME=scrapy
ARG UUID=1000
ARG GUID=${UUID}

RUN apt-get update -y \
    && apt-get install -y git sudo python3-pdm python3-pytest python3-pytest-cov python3-mypy python3-ipython \
    && addgroup --gid=${GUID} ${USERNAME} \
    && adduser --disabled-password --gecos "" --gid=${GUID} --uid=${UUID} ${USERNAME} \
    && echo "${USERNAME}    ALL=(root)   NOPASSWD:ALL" >/etc/sudoers.d/${USERNAME}

FROM base AS build
WORKDIR /usr/src/app
COPY . .
RUN pdm build

FROM build AS test
USER ${USERNAME}
WORKDIR /home/${USERNAME}

COPY --from=build --chown=${UUID}:${GUID} /usr/src/app/dist/ ./dist/

RUN python3 -m pip install --no-cache-dir scrapy ./dist/*.whl

COPY ./tests/scrapy_project ./scrapy_project
COPY ./tests/scrapy.cfg ./scrapy.cfg