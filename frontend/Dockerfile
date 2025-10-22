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
ARG BACKEND_API_URL
ENV BACKEND_API_URL=$BACKEND_API_URL

# Replace default NGINX config to support SPA routing and API proxy
COPY nginx.conf.template /etc/nginx/conf.d/default.conf.template

# Use template to insert Backend API host based on Env Var
RUN envsubst '${BACKEND_API_URL}' < /etc/nginx/conf.d/default.conf.template > /etc/nginx/conf.d/default.conf

EXPOSE 10000
CMD ["nginx", "-g", "daemon off;"]
