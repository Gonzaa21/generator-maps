import src.generator as generator
import src.visualizer as visualizer
import json
import numpy as np

# config.json
with open("config.json", "r") as file:
    config = json.load(file)

def Main():
    print("Generating map...")
    map = generator.generate_map(config["size"], config["scale"], config["octaves"], config["seed"])
    
    print("Saving map in npy file...")
    np.save("maps/npy/map.npy", map)

    print("Showing and saving image...")
    visualizer.visualizer_map(map)
    visualizer.save_map(map, config["output"])

    print("Process completed. Map saved in:", config["output"])

if __name__ == "__main__":
    Main()