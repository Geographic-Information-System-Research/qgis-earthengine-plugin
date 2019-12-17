import ee
from ee_plugin import Map

image = ee.ImageCollection('COPERNICUS/S2') \
  .filterDate('2017-01-01', '2017-01-02').median() \
  .divide(10000)
  
vis = {'bands': ['B12', 'B8', 'B4'], 'min': 0.05, 'max': 0.5}
  
Map.addLayer(image, vis, 'Sentinel-2 images January, 2018')

Map.setCenter(35.2, 31, 13)
