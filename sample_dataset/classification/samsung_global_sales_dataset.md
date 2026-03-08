About Dataset
15,500 synthetic sales transactions for Galaxy S, Z Fold/Flip, Galaxy A/M, Tablets, Watches, Buds, Smart TVs, Monitors & Appliances
across 52 countries, 555+ cities, sorted by Country → City → Date (2021 – 2024).

This dataset simulates a realistic global sales ledger for Samsung Electronics products.It spans flagship foldables to budget smartphones, smart home devices, and accessories —making it ideal for market segmentation, price analysis, 5G adoption tracking, time-series forecasting, and cross-country revenue analysis.

⚠️ All figures are synthetically generated for educational / portfolio purposes.
They do not represent actual Samsung Electronics financial data.

📁 File
File	Rows	Columns	Size
samsung_global_sales_dataset.csv	15,500	28	~3.7 MB
📋 Column Dictionary
#	Column	Type	Description
1	sale_id	string	Unique transaction ID —SAMS-XXXXXXXX
2	sale_date	date	Transaction date YYYY-MM-DD
3	year	int	2021 / 2022 / 2023 / 2024
4	quarter	string	Q1 / Q2 / Q3 / Q4
5	month	string	Full month name
6	country	string	Country of sale
7	region	string	Continent / geo-region
8	city	string	City of sale
9	product_name	string	Full product name
10	category	string	Galaxy S / Galaxy Z / Galaxy A / Galaxy M / Galaxy Tab / Galaxy Watch / Galaxy Buds / Monitor / Smart TV / Appliances / Accessories
11	storage	string	Storage variant (N/A for non-storage products)
12	color	string	Colour option
13	is_5g	string	Whether the device is 5G-capable: Yes / No
14	unit_price_usd	float	Per-unit list price in USD (±9 % market jitter)
15	discount_pct	float	Discount applied: 0, 2, 3, 5, 7, 10, 12, 15, or 20 %
16	units_sold	int	Quantity in this transaction (1–10, skewed toward 1)
17	discounted_price_usd	float	Effective per-unit price after discount
18	revenue_usd	float	Total transaction revenue in USD
19	currency	string	Local currency code
20	fx_rate_to_usd	float	Exchange rate used for conversion
21	revenue_local_currency	float	Revenue in local currency
22	sales_channel	string	Samsung Store / Online / Reseller / Carrier / Retailer / B2B / E-commerce
23	payment_method	string	Credit Card / Debit Card / Samsung Pay / EMI / Net Banking / Cash / Gift Card / BNPL
24	customer_segment	string	Individual / Business / Education / Government / Enterprise
25	customer_age_group	string	18–24 / 25–34 / 35–44 / 45–54 / 55+
26	previous_device_os	string	Buyer's previous OS (phones only; others →N/A)
27	customer_rating	float	Post-purchase rating 2.5–5.0; ~28 % are NaN
28	return_status	string	Kept / Returned / Exchanged
🌍 Countries Covered (52)
Region	Countries
North America	United States, Canada, Mexico
South America	Brazil, Argentina, Chile, Colombia, Peru
Europe	United Kingdom, Germany, France, Italy, Spain, Netherlands, Poland, Sweden, Switzerland, Norway, Denmark, Portugal, Austria, Belgium, Turkey, Russia, Ukraine, Romania, Czech Republic, Greece
Asia	India, China, South Korea, Japan, Indonesia, Pakistan, Bangladesh, Philippines, Vietnam, Thailand, Malaysia, Singapore, Taiwan, Myanmar, Sri Lanka
Middle East	Saudi Arabia, UAE, Egypt
Africa	South Africa, Nigeria, Kenya, Ethiopia
Oceania	Australia, New Zealand
📦 Products Covered (73)
Category	Count	Notable Models
Galaxy S	11	S21 FE · S22 · S23 · S24 series
Galaxy Z	5	Z Fold 4/5 · Z Flip 3/4/5
Galaxy A	9	A04 to A54 5G
Galaxy M	4	M04 to M54 5G
Galaxy Tab	7	Tab A9 to Tab S9 Ultra
Galaxy Watch	7	Watch 4 / 5 / 6 / FE / Classic
Galaxy Buds	4	Buds FE / Live / 2 / 2 Pro
Monitor	5	Odyssey G7 · Neo G9 · M8 · ViewFinity S9
Smart TV	6	Neo QLED · OLED · The Frame · Crystal UHD
Appliances	5	Fridge · Washer · Microwave · AC
Accessories	10	S Pen · Smart Tag · SSDs · Chargers · Cases
📊 Row Distribution
Category	Rows
Galaxy S	~2,316
Accessories	~2,101
Galaxy A	~1,892
Galaxy Tab	~1,524
Galaxy Watch	~1,486
Smart TV	~1,295
Galaxy Z	~1,058
Appliances	~1,052
Monitor	~1,046
Galaxy Buds	~869
Galaxy M	~861
Total	15,500
5G Capable: ~5,071 rows (33 %) | Non-5G: ~10,429 rows (67 %)

💡 Suggested Analyses
5G Adoption by Country — Which markets lead in 5G device sales?
Foldable Trends (Galaxy Z) — Growth of Z Fold vs Z Flip year-over-year
Budget vs Flagship Split — Galaxy A/M vs Galaxy S revenue share
Samsung Pay Adoption — Payment method preference by region
Revenue by City — Top 20 cities by total Samsung revenue
Category Mix — Phone vs TV vs Appliance share by country
Seasonality Analysis — Q4 vs Q1/Q2/Q3 across product lines
Discount Impact — Higher discount % → more units but lower margin?
OS Switching — What % of Galaxy S buyers switched from iOS?
Return Rate by Category — Which product has highest return rate?
Age Group Preferences — 18–24 prefers Galaxy A; 35+ prefers Galaxy S?
Multi-Year Trend — Revenue growth 2021 → 2024
🛠️ Generation Details
Script: generate_samsung_sales.py (Python 3, no external deps)
Seed: 99 — fully reproducible
Sort: Country → City → Date (ascending)
Date Range: January 2021 – December 2024 (4 years)
Prices: Based on real Samsung 2021–2024 pricing with ±9 % market jitter
FX Rates: Representative 2023 midpoint rates
Missing data: customer_rating is NaN for ~28 % of rows
Return status weights: Kept 86 % · Returned 9 % · Exchanged 5 %

Link : https://www.kaggle.com/datasets/ashyou09/samsung-global-product-sales-dataset
