FROM node:15.13-alpine
WORKDIR /react
COPY . .
RUN npm install --force --timeout=1800000
RUN npm run build
CMD ["npm", "run", "start"]