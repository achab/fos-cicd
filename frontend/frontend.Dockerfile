FROM node:10-alpine

WORKDIR /usr/src/app

RUN npm install

EXPOSE 8080

CMD [ "npm", "start" ]
