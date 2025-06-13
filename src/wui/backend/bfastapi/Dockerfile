FROM afc__api:0.5.0

WORKDIR /bfastapi

COPY requirements.txt main.py .
RUN pip3 install --no-cache-dir --break-system-packages -r requirements.txt

ENV UVICORN_HOST=0.0.0.0
ENV UVICORN_PORT=8000

EXPOSE 8000

CMD [ "python", "main.py"]
