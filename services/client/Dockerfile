FROM node:10.4.1-alpine

WORKDIR /usr/src/app

ENV PATH /usr/src/app/node_modules/.bin:$PATH

COPY package.json /usr/src/app/package.json

RUN npm install --silent
RUN npm install react-scripts@1.1.4 -g --silent
RUN npm install jquery@1.9.1  --silent
RUN npm install typescript --silent
RUN npm install react-bootstrap bootstrap --silent
RUN npm audit fix

COPY . .
CMD ["npm","start"]