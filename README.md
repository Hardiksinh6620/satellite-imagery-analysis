# Satellite Imagery Analysis

Raster workflows: NDVI, NDWI, zonal statistics, and change detection.

## Install
```bash
pip install -r requirements.txt
```

## Usage
```python
from src.indices import ndvi, ndwi
from src.zonal import zonal_stats

ndvi_arr = ndvi("data/red.tif", "data/nir.tif")
stats = zonal_stats(ndvi_arr, "data/zones.geojson")
```

## Provenance

See [HISTORY.md](HISTORY.md) for collaboration and reconstruction details.
