# syntax=docker/dockerfile:1

FROM ghcr.io/linuxserver/baseimage-alpine:3.21

# set version label
LABEL maintainer="groveld"

# environment settings
ENV FIREBIRD_VERSION=5.0.2.1613
ENV MATCHMAN_VERSION=0.1.0
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install packages
RUN \
    echo "**** install build packages ****" && \
    apk add --no-cache --upgrade --virtual=build-dependencies \
    tar \
    ca-certificates \
    libstdc++ \
    build-base \
    python3-dev && \
    echo "**** install runtime packages ****" && \
    apk add --no-cache --upgrade \
    python3 \
    gunicorn && \
    echo "**** install firebird ****" && \
    echo "**** install matchman ****" && \
    python3 -m venv /lsiopy && \
    pip install -U --no-cache-dir \
    pip \
    wheel && \
    pip install -U --no-cache-dir -r requirements.txt && \
    echo "**** cleanup ****" && \
    apk del --purge \
    build-dependencies && \
    rm -rf \
    /root/.cache \
    /tmp/*

# copy local files
COPY root/ /

# ports and volumes
EXPOSE 3000
VOLUME /config
