#!/bin/sh

curl -XPUT "http://opensearch-node1:9200/pnmindex" -H 'Content-Type: application/json' -d'
{
  "mappings": {
    "properties": {
      "location": {
        "type": "geo_shape"
      }
    }
  }
}'
