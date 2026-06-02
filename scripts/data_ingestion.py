import pandas as pd
import os

data_folder = "data/raw"

csv_files = [f for f in os.listdir(data_folder) if f.endswith(".csv")]

print(f"\nTotal Files Found: {len(csv_files)}")

for file in csv_files:

    print("\n" + "="*70)

    path = os.path.join(data_folder, file)

    try:
        df = pd.read_csv(path)

        print(f"\nFile: {file}")
        print(f"Shape: {df.shape}")

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

        print("\nFirst 5 Records:")
        print(df.head())

    except Exception as e:
        print(f"Error reading {file}")
        print(e)