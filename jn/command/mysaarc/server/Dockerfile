FROM node:latest
ENV NODE_ENV=production
WORKDIR /app
COPY ["code/package-lock.json", "code/package.json", "code/server.js", "./"]
RUN npm install --production
CMD [ "node", "server.js" ]