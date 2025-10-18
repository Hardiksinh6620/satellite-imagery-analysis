"""Zonal statistics over raster + vector."""
import numpy as np
import rasterio
from rasterio.mask import mask
import geopandas as gpd

def zonal_stats(raster_path, vector_path, stat="mean"):
    with rasterio.open(raster_path) as src:
        gdf = gpd.read_file(vector_path).to_crs(src.crs)
        out = []
        for _, row in gdf.iterrows():
            try:
                clipped, _ = mask(src, [row.geometry], crop=True)
                vals = clipped[0][~np.isnan(clipped[0])]
                out.append(float(getattr(np, stat)(vals)) if vals.size else None)
            except Exception:
                out.append(None)
        return out
