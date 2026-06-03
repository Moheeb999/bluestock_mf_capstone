from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

# Database location
DB_PATH = "data/db/bluestock_mf.db"

# Create SQLite connection
engine = create_engine(f"sqlite:///{DB_PATH}")

# Processed data folder
processed_path = Path("data/processed")

csv_files = sorted(processed_path.glob("*.csv"))

print(f"Found {len(csv_files)} CSV files")

for file in csv_files:

    print(f"\nLoading {file.name}")

    df = pd.read_csv(file)

    table_name = file.stem

    # Remove numbering prefixes
    for prefix in [
        "01_", "02_", "03_", "04_", "05_",
        "06_", "07_", "08_", "09_", "10_"
    ]:
        table_name = table_name.replace(prefix, "")

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"Loaded into table: {table_name}")

print("\nDatabase created successfully!")