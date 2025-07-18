"""Raster metadata inspection."""
import rasterio
def metadata(path):
    with rasterio.open(path) as src:
        return {"crs":str(src.crs),"width":src.width,"height":src.height,"count":src.count,"dtype":str(src.dtypes[0]),"nodata":src.nodata,"transform":tuple(src.transform)}
