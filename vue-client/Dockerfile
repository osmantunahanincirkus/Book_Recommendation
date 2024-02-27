FROM node:18-alpine3.18 AS base

#############################################################################################
FROM base AS deps

ARG TZ='Europe/Istanbul'
ENV TZ ${TZ}
RUN apk upgrade --update \
    && apk add -U tzdata \
    && cp /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo "${TZ}" > /etc/timezone \
    && apk del tzdata \
    && rm -rf \
    /var/cache/apk/*

#############################################################################################
FROM deps AS vue

WORKDIR /app

COPY ./vue-client/package*.json .

RUN npm install

#############################################################################################
FROM vue AS prod

WORKDIR /app

COPY ./vue-client /app
RUN npm run build

VOLUME /app

EXPOSE 80

ENV HOST=0.0.0.0
ENV PORT=80

RUN export TZ=${TZ}

CMD ["npm", "run", "preview"]

#############################################################################################
FROM prod
