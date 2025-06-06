FROM alpine:3.22.0

WORKDIR /afc

RUN apk add --no-cache ffmpeg python3 py3-pip

ADD src ./src
COPY pyproject.toml requirements.txt .

RUN pip3 install --no-cache-dir --break-system-packages -r requirements.txt
RUN pip3 install --no-cache-dir --break-system-packages .
