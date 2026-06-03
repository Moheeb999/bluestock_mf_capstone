-- Star Schema for Bluestock Mutual Fund Capstone

CREATE TABLE dim_fund (
amfi_code INTEGER PRIMARY KEY,
scheme_name TEXT,
fund_house TEXT,
category TEXT,
sub_category TEXT,
plan TEXT,
risk_category TEXT
);

CREATE TABLE dim_date (
date_id INTEGER PRIMARY KEY,
full_date DATE,
year INTEGER,
month INTEGER,
quarter INTEGER
);

CREATE TABLE fact_nav (
amfi_code INTEGER,
nav_date DATE,
nav REAL,
FOREIGN KEY(amfi_code)
REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_transactions (
investor_id TEXT,
transaction_date DATE,
amfi_code INTEGER,
transaction_type TEXT,
amount_inr REAL,
state TEXT,
city TEXT,
kyc_status TEXT,
FOREIGN KEY(amfi_code)
REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_performance (
amfi_code INTEGER,
return_1yr_pct REAL,
return_3yr_pct REAL,
return_5yr_pct REAL,
alpha REAL,
beta REAL,
sharpe_ratio REAL,
expense_ratio_pct REAL,
FOREIGN KEY(amfi_code)
REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_aum (
fund_house TEXT,
report_date DATE,
aum_crore REAL,
num_schemes INTEGER
);
