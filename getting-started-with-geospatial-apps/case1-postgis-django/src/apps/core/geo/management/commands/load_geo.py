
from pathlib import Path
from django.conf import settings
from django.contrib.gis.gdal import DataSource
from django.contrib.gis.utils import LayerMapping
from django.core.management.base import BaseCommand 
from apps.core.geo.models import WorldBorder

world_mapping = {
    "fips": "FIPS",
    "iso2": "ISO2",
    "iso3": "ISO3",
    "un": "UN",
    "name": "NAME",
    "area": "AREA",
    "pop2005": "POP2005",
    "region": "REGION",
    "subregion": "SUBREGION",
    "lon": "LON",
    "lat": "LAT",
    "mpoly": "MULTIPOLYGON",
}

class Command(BaseCommand): 
    help = 'Load World Border Data'
  
    def handle(self, *args, **kwargs):
        verbose = True
        world_shp = Path(settings.BASE_DIR).resolve().parent / "src" / "data" / "TM_WORLD_BORDERS-0.3.shp"
        lm = LayerMapping(WorldBorder, world_shp, world_mapping, transform=False)
        lm.save(strict=True, verbose=verbose)        