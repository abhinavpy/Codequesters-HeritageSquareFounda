# 1) Build stage
FROM node:20-alpine AS builder
WORKDIR /app

# copy package manifests and install deps
COPY package.json package-lock.json ./
RUN npm ci

# copy source & build
COPY . .
RUN npm run build

# 2) Production stage
FROM nginx:stable-alpine
# remove default site
RUN rm /etc/nginx/conf.d/default.conf
# copy a minimal SPA‐friendly nginx config
COPY nginx.conf /etc/nginx/conf.d
# copy built assets
COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]