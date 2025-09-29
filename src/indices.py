"""Spectral indices with alignment and nodata checks."""
import numpy as np
import rasterio

def _read(path):
    with rasterio.open(path) as src:
        return src.read(1, masked=True).astype("float32"), src.profile

def normalized_difference(a, b):
    a=np.ma.asarray(a,dtype="float32"); b=np.ma.asarray(b,dtype="float32")
    denom=a+b
    return np.ma.masked_where(denom==0,(a-b)/denom)

def _pair(first_path, second_path):
    first,p1=_read(first_path); second,p2=_read(second_path)
    for key in ("width","height","transform","crs"):
        if p1.get(key)!=p2.get(key): raise ValueError(f"Raster {key} values do not match")
    return first,second,p1

def ndvi(red_path,nir_path):
    red,nir,_=_pair(red_path,nir_path); return normalized_difference(nir,red)

def ndwi(green_path,nir_path):
    green,nir,_=_pair(green_path,nir_path); return normalized_difference(green,nir)

def change_detection(before_path,after_path,threshold=0.1):
    before,after,_=_pair(before_path,after_path); return np.ma.abs(after-before)>threshold
