from pathlib import Path
import pandas as pd

# ==========================================
# PATH CONFIGURATION
# ==========================================

RAW_PATH = Path("data/raw")
PROCESSED_PATH = Path("data/processed")

PROCESSED_PATH.mkdir(
    parents=True,
    exist_ok=True
)

# ==========================================
# LOAD ALL CSV FILES
# ==========================================

csv_files = sorted(
    RAW_PATH.glob("*.csv")
)

print("=" * 80)
print("BLUESTOCK MUTUAL FUND ETL PIPELINE")
print("=" * 80)

print(f"\nFound {len(csv_files)} CSV files\n")

# ==========================================
# PROCESS EACH FILE
# ==========================================

for file in csv_files:

    print("\n" + "=" * 80)
    print(f"PROCESSING: {file.name}")
    print("=" * 80)

    try:

        # -----------------------------
        # LOAD DATA
        # -----------------------------

        df = pd.read_csv(file)

        # ==========================================
        # DAY 2 CLEANING
        # ==========================================

        # NAV HISTORY

        if file.name == "02_nav_history.csv":

            print("\nCleaning NAV History...")

            df["date"] = pd.to_datetime(
                df["date"],
                errors="coerce"
            )

            df = df.sort_values(
                ["amfi_code", "date"]
            )

            df = df.drop_duplicates()

            df = df[
                df["nav"] > 0
            ]

            df["nav"] = (
                df.groupby("amfi_code")["nav"]
                .ffill()
            )

        # INVESTOR TRANSACTIONS

        if file.name == "08_investor_transactions.csv":

            print("\nCleaning Investor Transactions...")

            df["transaction_date"] = pd.to_datetime(
                df["transaction_date"],
                errors="coerce"
            )

            valid_types = [
                "Sip",
                "Lumpsum",
                "Redemption"
            ]

            df["transaction_type"] = (
                df["transaction_type"]
                .astype(str)
                .str.strip()
                .str.title()
            )

            df = df[
                df["transaction_type"]
                .isin(valid_types)
            ]

            df = df[
                df["amount_inr"] > 0
            ]

            valid_kyc = [
                "Verified",
                "Pending"
            ]

            invalid_kyc = df[
                ~df["kyc_status"]
                .isin(valid_kyc)
            ]

            print(
                f"Invalid KYC Records: {len(invalid_kyc)}"
            )

        # SCHEME PERFORMANCE

        if file.name == "07_scheme_performance.csv":

            print("\nCleaning Scheme Performance...")

            return_cols = [
                "return_1yr_pct",
                "return_3yr_pct",
                "return_5yr_pct"
            ]

            for col in return_cols:

                if col in df.columns:

                    df[col] = pd.to_numeric(
                        df[col],
                        errors="coerce"
                    )

            if "expense_ratio_pct" in df.columns:

                anomalies = df[
                    (
                        df["expense_ratio_pct"] < 0.1
                    )
                    |
                    (
                        df["expense_ratio_pct"] > 2.5
                    )
                ]

                print(
                    f"Expense Ratio Anomalies: {len(anomalies)}"
                )

        # -----------------------------
        # BASIC INFO
        # -----------------------------

        print("\nShape:")
        print(df.shape)

        print("\nColumns:")
        print(list(df.columns))

        # -----------------------------
        # CHECK MISSING VALUES
        # -----------------------------

        print("\nMissing Values:")

        missing = df.isnull().sum()

        print(missing)

        total_missing = missing.sum()

        print(
            f"\nTotal Missing Values: {total_missing}"
        )

        # -----------------------------
        # CONVERT DATE COLUMNS
        # -----------------------------

        date_columns = [
            "date",
            "launch_date",
            "transaction_date",
            "portfolio_date",
            "month"
        ]

        for col in date_columns:

            if col in df.columns:

                print(
                    f"\nConverting {col} to datetime..."
                )

                if (
                    "bluechip_nav" in file.name.lower()
                    or "largecap_nav" in file.name.lower()
                    or "top100_nav" in file.name.lower()
                ):

                    df[col] = pd.to_datetime(
                        df[col],
                        errors="coerce",
                        dayfirst=True
                    )

                else:

                    df[col] = pd.to_datetime(
                        df[col],
                        errors="coerce"
                    )

                invalid_dates = (
                    df[col]
                    .isnull()
                    .sum()
                )

                if invalid_dates > 0:

                    print(
                        f"Warning: {invalid_dates} invalid dates found in {col}"
                    )

        # -----------------------------
        # REMOVE DUPLICATES
        # -----------------------------

        before = len(df)

        df = df.drop_duplicates()

        after = len(df)

        duplicates_removed = (
            before - after
        )

        print(
            f"\nDuplicates Removed: {duplicates_removed}"
        )

        # -----------------------------
        # SAVE CLEAN DATA
        # -----------------------------

        output_file = (
            PROCESSED_PATH /
            file.name
        )

        df.to_csv(
            output_file,
            index=False
        )

        print(
            "\nSaved Clean File:"
        )

        print(output_file)

        print(
            f"\nCompleted {file.name}"
        )

    except Exception as e:

        print(
            f"\nERROR processing {file.name}"
        )

        print(e)

# ==========================================
# PIPELINE COMPLETE
# ==========================================

print("\n" + "=" * 80)
print("ETL PIPELINE COMPLETED SUCCESSFULLY")
print("=" * 80)