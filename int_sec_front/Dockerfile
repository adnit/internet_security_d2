FROM node:16 AS development

RUN mkdir -p /usr/src/nuxt
WORKDIR /usr/src/nuxt

COPY . /usr/src/nuxt/
RUN rm -rf /tmp/nitro/worker*

RUN npm install


EXPOSE 3002

CMD [ "yarn", "dev" ]