import rasterio
from rasterio.io import MemoryFile
from rasterio.transform import from_origin
from src.io import metadata
def test_metadata(tmp_path):
    path=tmp_path/"sample.tif"
    with rasterio.open(path,"w",driver="GTiff",width=2,height=2,count=1,dtype="uint8",crs="EPSG:4326",transform=from_origin(0,2,1,1),nodata=0) as dst: dst.write([[1,2],[3,4]],1)
    info=metadata(path); assert info["width"]==2 and info["nodata"]==0
