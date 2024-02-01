import requests
import uuid
import json

url = "http://opensearch-node1:9200/pnmindex/_doc"
headers = {"Content-Type": "application/json"}
with open("data/schools.geojson", "r") as geojson_file:
    geojson_data = json.load(geojson_file)
    for d in geojson_data["features"]:
        print(d)
        if "node" in d["properties"]["@id"]:
            d["id"] = str(uuid.uuid4())
            r = requests.put(url + "/" + d["id"], json=d)
            print(r.text)
