FROM node:16
COPY ./package.json /src/
WORKDIR /src
RUN npm install
COPY . /src
USER www-data
CMD ["npm", "start"]
