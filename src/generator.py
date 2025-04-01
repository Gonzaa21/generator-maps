import random
import time
import numpy as np
import json
from perlin_noise import PerlinNoise

# configuration
with open('config.json','r') as file:
    config = json.load(file)
    
# generate function
def generate_map(size, scale, octaves):
    seed = int(time.time())
    noise = PerlinNoise(octaves=octaves, seed=seed) # adding octaves and seed
    map = np.array([[noise([i / scale, j / scale]) for j in range(size)] for i in range(size)]) # adding size and scale
    
    # The perlin noise can generate anonymous values, to not have distorsions 
    # and errors, we have to normalize values in range 0-1. The normalization is
    # based on the following formula: normal_value = value - min_value / max_value - min_value
    map = (map - map.min()) / (map.max() - map.min())
    return map

# save binary map
def gen_save_map(map_data):
    timestamp = time.strftime("%Y%m%d_%H%M%S")  # Generate unique label based on date
    filename = f"maps/bin/map_{timestamp}.bin"

    with open(filename, "wb") as f:
        np.save(f, map_data)  # Save in binary

    return filename