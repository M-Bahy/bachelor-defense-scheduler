FROM node:15.13-alpine
WORKDIR /react
COPY . .
RUN npm i
RUN npm run build
CMD ["npm", "run", "start"]