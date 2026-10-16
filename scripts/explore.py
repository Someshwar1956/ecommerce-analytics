import glob, os
import pandas as pd

for path in sorted(glob.glob("data/raw/*.csv")):
    df = pd.read_csv(path)
    print("=" * 60)
    print(os.path.basename(path))
    print("rows:", len(df), "| columns:", len(df.columns))
    print(list(df.columns))
    print(df.head(2).to_string())