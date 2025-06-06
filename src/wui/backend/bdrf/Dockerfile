FROM afc:0.5.0

WORKDIR /bdrf

COPY requirements.txt .
RUN pip3 install --no-cache-dir --break-system-packages -r requirements.txt
COPY . .

ARG GUNICORN_HOST=0.0.0.0
ARG GUNICORN_PORT=8000

ENV GUNICORN_CMD_ARGS="--bind=${GUNICORN_HOST}:${GUNICORN_PORT}"

EXPOSE 8000

CMD [ "gunicorn", "bdrf.wsgi" ]
