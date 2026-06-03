# Bluestock Mutual Fund Data Dictionary

## fund_master

| Column            | Data Type | Description                   |
| ----------------- | --------- | ----------------------------- |
| amfi_code         | INTEGER   | Unique AMFI scheme identifier |
| fund_house        | TEXT      | Mutual fund company           |
| scheme_name       | TEXT      | Name of scheme                |
| category          | TEXT      | Equity, Debt, etc.            |
| sub_category      | TEXT      | Large Cap, Small Cap, etc.    |
| plan              | TEXT      | Direct or Regular             |
| launch_date       | DATE      | Scheme launch date            |
| expense_ratio_pct | FLOAT     | Expense ratio percentage      |
| risk_category     | TEXT      | Risk classification           |

## nav_history

| Column    | Data Type | Description     |
| --------- | --------- | --------------- |
| amfi_code | INTEGER   | Scheme code     |
| date      | DATE      | NAV date        |
| nav       | FLOAT     | Net Asset Value |

## investor_transactions

| Column           | Data Type | Description              |
| ---------------- | --------- | ------------------------ |
| investor_id      | TEXT      | Investor identifier      |
| transaction_date | DATE      | Transaction date         |
| transaction_type | TEXT      | SIP, Lumpsum, Redemption |
| amount_inr       | FLOAT     | Transaction amount       |
| state            | TEXT      | Investor state           |
| city             | TEXT      | Investor city            |
| kyc_status       | TEXT      | KYC verification status  |

## scheme_performance

| Column            | Data Type | Description          |
| ----------------- | --------- | -------------------- |
| return_1yr_pct    | FLOAT     | One year return      |
| return_3yr_pct    | FLOAT     | Three year return    |
| return_5yr_pct    | FLOAT     | Five year return     |
| alpha             | FLOAT     | Alpha metric         |
| beta              | FLOAT     | Beta metric          |
| sharpe_ratio      | FLOAT     | Risk-adjusted return |
| expense_ratio_pct | FLOAT     | Expense ratio        |

## aum_by_fund_house

| Column      | Data Type | Description             |
| ----------- | --------- | ----------------------- |
| date        | DATE      | Reporting date          |
| fund_house  | TEXT      | Fund house              |
| aum_crore   | FLOAT     | Assets under management |
| num_schemes | INTEGER   | Number of schemes       |
