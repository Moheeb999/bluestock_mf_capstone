-- 1. Top 5 fund houses by AUM
SELECT fund_house,
SUM(aum_crore) AS total_aum
FROM aum_by_fund_house
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;

-- 2. Average NAV by month
SELECT strftime('%Y-%m', date) AS month,
AVG(nav) AS avg_nav
FROM nav_history
GROUP BY month;

-- 3. Monthly SIP inflow trend
SELECT month,
sip_inflow_crore
FROM monthly_sip_inflows
ORDER BY month;

-- 4. Transactions by state
SELECT state,
COUNT(*) AS transaction_count
FROM investor_transactions
GROUP BY state
ORDER BY transaction_count DESC;

-- 5. Funds with expense ratio below 1%
SELECT scheme_name,
expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1;

-- 6. Average 3-year return by category
SELECT category,
AVG(return_3yr_pct)
FROM scheme_performance
GROUP BY category;

-- 7. Risk grade distribution
SELECT risk_grade,
COUNT(*)
FROM scheme_performance
GROUP BY risk_grade;

-- 8. Number of schemes per fund house
SELECT fund_house,
COUNT(*) AS scheme_count
FROM fund_master
GROUP BY fund_house
ORDER BY scheme_count DESC;

-- 9. Maximum NAV recorded
SELECT MAX(nav)
FROM nav_history;

-- 10. Minimum NAV recorded
SELECT MIN(nav)
FROM nav_history;
