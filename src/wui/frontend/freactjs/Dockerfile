FROM node:18.19.1-alpine

WORKDIR /freactjs

COPY . .

RUN npm install

ARG VITE_HOST=0.0.0.0
ARG VITE_PORT=5175
ENV VITE_HOST=${VITE_HOST}
ENV VITE_PORT=${VITE_PORT}

EXPOSE ${VITE_PORT}

CMD [ "npm", "run", "dev" ]