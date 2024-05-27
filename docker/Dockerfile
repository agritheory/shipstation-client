FROM python:3.10-slim-bullseye

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 PATH="${PATH}:/root/.poetry/bin:/root/.local/bin"

RUN apt-get update
RUN apt-get install -y --no-install-recommends curl make
RUN rm -rf /var/lib/apt/lists/*

COPY Makefile pyproject.toml ./

RUN make download-poetry
RUN make install NO_PRE_COMMIT=1
RUN rm Makefile pyproject.toml

CMD mkdir -p /workspace
WORKDIR /workspace
