# Stage 1: Build the Vue app
FROM node:22-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Stage 2: Serve with NGINX
FROM nginx:stable-alpine
COPY --from=builder /app/dist /usr/share/nginx/html

# Install envsubst (part of gettext)
RUN apk add --no-cache gettext

# Accept env vars
ARG BACKEND_HOST
ARG NGINX_CONF
ENV BACKEND_HOST=$BACKEND_HOST
ENV NGINX_CONF=$NGINX_CONF

# Copy both configs
COPY nginx.local.conf /etc/nginx/conf.d/nginx.local.conf.template
COPY nginx.prod.conf /etc/nginx/conf.d/nginx.prod.conf.template

# Use envsubst to generate the active config
RUN envsubst '${BACKEND_HOST}' < /etc/nginx/conf.d/${NGINX_CONF}.template > /etc/nginx/conf.d/default.conf

EXPOSE 10000
CMD ["nginx", "-g", "daemon off;"]
