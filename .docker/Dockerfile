# syntax=docker/dockerfile:1

FROM ghcr.io/linuxserver/baseimage-alpine:3.21

# set version label
ARG BUILD_DATE
ARG VERSION
LABEL build_version="Linuxserver.io version:- ${VERSION} Build-date:- ${BUILD_DATE}"
LABEL maintainer="groveld"

# environment settings
ARG RADARR_BRANCH="master"
ENV XDG_CONFIG_HOME="/config/xdg"

RUN \
    echo "**** install packages ****" && \
    apk add -U --upgrade --no-cache \
    python3 \
    echo "**** install pyload ****" && \
    mkdir -p /app/matchman/bin && \
    echo "**** cleanup ****" && \
    rm -rf \
    /root/.cache \
    /tmp/*

# add local files
COPY root/ /

# ports and volumes
EXPOSE 3000
VOLUME /config
