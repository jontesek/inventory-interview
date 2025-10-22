# Inventory Editor
App for listing and editing of products from eshop inventory

## Local usage

1. Create `.env` file containing `API_TOKEN` variable (see [template.env](./template.env) for example).
2. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
3. Run `docker-compose up` command (in root dir, wait for finish)
4. See the app: http://localhost:5000/products 

## Description

### Action flow
Show products:
1. Request products in Inventory - save product ids
2. Request product details for all ids
3. Show all info in table

Edit product:
1. Click on edit button
2. Update value
3. Click on save button
4. Data is saved to API and updated reactively in UI

### App structure

* Backend: Written in Python, using FastAPI. It communicates with the Baselinker API.
* Frontend: Written in Javascript, using Vue.js. It communicates with the Backend API.

When run with Docker, the frontend is served by Nginx server.

## TODO

* UI: Choose Inventory ID
* Authentication (for frontend and backend)
* Product price: Select default price group from API (now hardcoded)
