import json
from tqdm import tqdm

# This file creates a large .json file as example

N_KEYS = 1_000_000

data = {}
for x in tqdm(range(N_KEYS)):
    data[f"key_{x}"] = f"value_{x}"

with open("example.json", "w") as f:
    json.dump(data, f, indent=2)
