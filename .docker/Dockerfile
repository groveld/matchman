# syntax=docker/dockerfile:1

FROM ghcr.io/linuxserver/baseimage-ubuntu:noble

# set version label
LABEL maintainer="groveld"

# environment settings
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# copy local files
COPY root/ /

# install packages
RUN \
    echo "**** install runtime dependencies ****" && \
    apt-get update && \
    apt-get install -y \
    python3 \
    python3-pip \
    gunicorn \
    libtommath1 && \
    echo "**** install matchman ****" && \
    pip install --upgrade --no-cache-dir /app/matchman-0.1.0-py3-none-any.whl --break-system-packages && \
    echo "**** clean up ****" && \
    apt-get clean && \
    rm -rf \
    /root/.cache \
    /tmp/* \
    /var/lib/apt/lists/* \
    /var/tmp/*

# ports and volumes
EXPOSE 3000
VOLUME /config
