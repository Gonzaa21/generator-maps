import hashlib
import json
import os
import src.generator as generator

def generate_hash(filename): # generate hash
    hasher = hashlib.sha256() # create hash with SHA-256
    
    # open bin file, read the folder in parts (blocks of maximum 4096bytes) and 
    # each block read, will be added to hash. The loop breaks when the last block is empty
    with open(filename, "rb") as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
            
    return hasher.hexdigest() # return hash in hex format for more readability

def save_hash(map_filename): # save hash in json
    hash_value = generate_hash(map_filename) # generate hash
    hash_filename = f'maps/hash/{os.path.basename(map_filename)}'.replace(".bin", ".json") # save route and replace .bin -> .json

    with open(hash_filename, "w") as f: # add hash value in json file
        json.dump({"hash": hash_value}, f)

    return hash_filename

if __name__ == "__main__":
    map_filename = generator.gen_save_map(map)  # save map
    hash_filename = save_hash(map_filename)  # generate and save hash