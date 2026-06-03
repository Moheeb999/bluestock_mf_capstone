from pathlib import Path
import pandas as pd

raw_path = Path("data/raw")

csv_files = sorted(raw_path.glob("*.csv"))

print(f"\nFound {len(csv_files)} CSV files\n")

for file in csv_files:
    print("=" * 80)
    print(f"FILE: {file.name}")

    try:
        df = pd.read_csv(file)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

    except Exception as e:
        print(f"Error reading file: {e}")

    print("\n")