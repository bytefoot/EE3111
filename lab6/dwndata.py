from ucimlrepo import fetch_ucirepo
import pandas as pd
import os

# fetch dataset
concrete_compressive_strength = fetch_ucirepo(id=165)

# data
X = concrete_compressive_strength.data.features
y = concrete_compressive_strength.data.targets

# combine features + target into one dataframe
df = pd.concat([X, y], axis=1)

os.makedirs("./data", exist_ok=True)

# export CSV
df.to_csv("./data/concrete_data.csv", index=False)

def pretty_write(d, f, indent=0):
    for key, value in d.items():
        prefix = "\t" * indent
        if isinstance(value, dict):
            f.write(f"{prefix}{key}:\n")
            pretty_write(value, f, indent + 1)
        elif isinstance(value, list):
            f.write(f"{prefix}{key}:\n")
            for item in value:
                if isinstance(item, dict):
                    pretty_write(item, f, indent + 1)
                else:
                    f.write(f"{prefix}\t- {item}\n")
        else:
            f.write(f"{prefix}{key}: {value}\n")

# export metadata + variables to txt
with open("./data/metadata.txt", "w") as f:
    f.write("=== METADATA ===\n")
    pretty_write(concrete_compressive_strength.metadata, f)
    f.write("\n\n=== VARIABLES ===\n")
    f.write(str(concrete_compressive_strength.variables))