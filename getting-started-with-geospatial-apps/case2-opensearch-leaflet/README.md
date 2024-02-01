# Opensearch x Leaflet

The following is a template on how to use Opensearch and Leaflet. Opensearch is an alterantive to Elasticsearch that focuses on a more community driven development. Leaflet is a Javascript library that allows to develop interactive maps.

## Components

- Opensearch
- Leaflet

## Setup

1. Run the application.
   ```
   docker compose up
   ```
2. Login to the `leaflet` container.
   ```
   docker exec -it leaflet bash
   bash load_mapping.sh
   python utils/load_data.py
   ```
3. Open your browser and go to `http://localhost:7600/`

## Activities

- Learn how elements are being added to the map using leaflet
- Learn how to query data from an endpoint
