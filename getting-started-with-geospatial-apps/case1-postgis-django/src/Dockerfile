FROM python:3.11.6-slim
ENV PYTHONUNBUFFERED 1
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc g++ libgeos-dev libgdal-dev gdal-bin proj-bin libproj-dev netcat-traditional\
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /src
WORKDIR /src
ADD requirements.txt /src
RUN pip install -r requirements.txt && \
    pip install --timeout=1000 --global-option=build_ext --global-option="-I/usr/include/gdal" GDAL==3.6.0
ADD . /src/

ENTRYPOINT ["/src/entrypoint.sh"]