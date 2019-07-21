FROM node:latest

# Create app directory
RUN mkdir -p /app
WORKDIR /app

COPY package.json /app/

RUN yarn global add expo-cli
RUN yarn install

CMD [ "yarn", "start" ]