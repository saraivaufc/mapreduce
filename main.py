import glob

import numpy as np

from mapreduce import MapReduce

input_images = folders = [f for f in glob.glob("data/LC08*.tif", recursive=True)]

output_image = "data/output.tif"

def map_func(image):
    nir = image[0:1, :, :]
    red = image[2:3, :, :]
    ndvi = (nir - red) / (nir + red + 0.000001)
    ndvi = np.array(ndvi * 1000).astype(np.int32)
    return ndvi


def reduce_func(images):
    return np.max(images, axis=0)


mapreduce = MapReduce(
    input_images=input_images,
    output_image=output_image,
    map_func=map_func,
    reduce_func=reduce_func
)

mapreduce.run()
