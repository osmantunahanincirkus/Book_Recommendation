FROM node:16-alpine3.16

ARG TZ='Europe/Istanbul'
ENV TZ ${TZ}
RUN apk upgrade --update \
    && apk add -U tzdata \
    && cp /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo "${TZ}" > /etc/timezone \
    && apk del tzdata \
    && rm -rf \
    /var/cache/apk/*

WORKDIR /app

COPY ./api/package*.json ./

RUN npm install

COPY ./api .

EXPOSE 3008

RUN export TZ=${TZ}

CMD [ "node", "index.js" ]