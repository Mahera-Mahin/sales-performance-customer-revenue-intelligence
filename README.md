# Sales Performance, Customer & Revenue Intelligence Platform

A portfolio-grade **Business Intelligence and analytics platform** demonstrating data quality validation, SQL analytics, KPI reporting, customer intelligence, root-cause analysis, statistical testing, trend analysis, and executive decision support.

> **Dataset:** Reproducible synthetic sales data created specifically for this portfolio project. It is not Cummins data and does not represent actual Cummins performance.

---

## Business Problem

Sales organizations need to understand not only **what happened**, but also:

- Are regions achieving their sales targets?
- Which products are driving revenue and margin?
- Which customer segments contribute the most value?
- Where are the largest performance gaps?
- What factors are driving underperformance?
- Is performance improving or deteriorating over time?
- Which areas should management prioritize?

This project builds an end-to-end analytical workflow to answer these questions and convert operational sales data into actionable business insights.

---

## Business Workflow

```text
Raw Transactions
       ↓
Data Quality Validation
       ↓
PostgreSQL Staging
       ↓
Analytical Star Schema
       ↓
SQL KPI & Performance Layer
       ↓
Python EDA & Statistical Analysis
       ↓
Power BI Reporting
       ↓
Root-Cause Analysis
       ↓
Management Recommendations
Dataset
50,000 sales transactions
2,200 customers
5 regions
8 products/product families
2023–2025 historical period
Revenue, cost, margin, discount and target information
Customer segment, industry, city and regional attributes
Key Validated Results

Analysis of completed orders produced the following validated portfolio-level KPIs:

KPI	Result
Completed Orders	47,017
Active Customers	2,200
Revenue	8.67B
Gross Margin	1.83B
Gross Margin %	21.16%
Average Order Value	184,334

The analytical results were independently reconciled between the Python processing pipeline and PostgreSQL.

Root-Cause Analysis Example

A regional/category drill-down identified an important 2025 performance gap:

East
  ↓
Engines
  ↓
Industrial Engines
Finding
Metric	Result
Revenue	116.54M
Target	125.14M
Attainment	93.13%
Target Gap	-8.60M
Gross Margin	18.46M
Margin %	15.84%

The analysis demonstrates a structured drill-down from:

Region → Category → Product → Customer Segment

rather than stopping at high-level KPI reporting.

This approach helps identify where performance is below target and what level of the business hierarchy requires further investigation.

Customer Intelligence

The customer analysis evaluates:

Customer revenue
Customer segment contribution
Revenue per customer
Order activity
Gross margin
Average order value
Regional and industry performance

Customer segments were analyzed to understand both revenue contribution and customer-level economics.

Product Intelligence

The product analysis evaluates:

Revenue
Units sold
Gross margin
Margin %
Revenue per unit
Product/category contribution
Target attainment

This supports identification of high-revenue products as well as products with stronger or weaker profitability.

Regional Intelligence

Regional analysis includes:

Revenue
Target
Target attainment
Target gap
Gross margin
Margin %
Year-over-year performance
Region/category root-cause analysis

The analysis can be drilled down from regional performance into individual categories and products.

Trend Analysis

The monthly analytical layer evaluates:

Monthly revenue
Monthly target
Target attainment
Target gap
Gross margin
Margin %
Month-over-month growth
Year-over-year growth
Monthly order and customer activity

This allows management to distinguish between isolated performance fluctuations and sustained trends.

Statistical Analysis

The project includes hypothesis testing using one-way ANOVA to evaluate whether average order value differs significantly across customer segments.

The analysis provides statistical evidence to complement descriptive KPI reporting rather than relying solely on visual differences.

Data Quality & Validation

The project implements automated data-quality checks covering:

Duplicate order IDs
Null customer keys
Null product keys
Invalid sales values
Invalid units
Invalid discount percentages
Gross-margin reconciliation
Invalid order statuses
Missing order dates

The Python data-quality pipeline reports:

All data-quality checks passed.

Automated tests are also included under:

tests/
└── test_data_quality.py
PostgreSQL Analytical Architecture

The project uses PostgreSQL as the analytical database layer.

                    dim_date
                       │
                       │
dim_customer ──── fact_sales ──── dim_product
                       │
                       │
                  dim_region

                  fact_targets
Data model
dim_customer — customer attributes and segmentation
dim_product — product/category information
dim_region — regional dimension
dim_date — date/calendar dimension
fact_sales — transactional sales data
fact_targets — regional/category sales targets

The dimensional structure supports reusable SQL analysis and BI reporting.

SQL Analytical Layer
sql/
├── 01_schema.sql
├── 02_kpi_queries.sql
├── 03_data_quality_checks.sql
├── 04_customer_performance.sql
├── 05_product_performance.sql
├── 06_region_category_performance.sql
└── 07_monthly_performance.sql

The SQL layer provides reusable analytical queries for:

Executive KPIs
Customer performance
Product performance
Regional/category performance
Root-cause analysis
Monthly performance
Target attainment
Margin analysis
Trend analysis
Python Analytics Pipeline
src/
├── 01_data_quality.py
├── 02_eda_and_kpis.py
├── 03_hypothesis_testing.py
└── 04_root_cause_analysis.py
Python capabilities
Data validation
Exploratory data analysis
KPI generation
Customer segmentation analysis
Product analysis
Regional analysis
Statistical hypothesis testing
Root-cause analysis
Analytical output generation
Power BI

Power BI is used as the executive reporting and visualization layer.

The dashboard is designed around:

Executive KPIs
Revenue performance
Gross margin
Target attainment
Regional performance
Product performance
Customer segmentation
Trend analysis
Root-cause analysis

Supporting documentation is available under:

powerbi/
├── BUILD_GUIDE.md
└── DAX_Measures.md

The Power BI layer is designed to translate the underlying SQL and analytical outputs into decision-oriented reporting.

Technology Stack

Python · Pandas · NumPy · PostgreSQL · SQL · Power BI · DAX · Power Query · Excel · Git/GitHub

Repository Structure
sales-performance-customer-revenue-intelligence/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── sql/
│
├── src/
│
├── tests/
│
├── powerbi/
│
├── docs/
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
Running the Python Pipeline

Create and activate a virtual environment, then install dependencies:

pip install -r requirements.txt

Run the analytical pipeline:

python src/01_data_quality.py
python src/02_eda_and_kpis.py
python src/03_hypothesis_testing.py
python src/04_root_cause_analysis.py

Run automated tests:

pytest
Example Business Questions Answered

The platform is designed to answer questions such as:

Are we achieving our sales targets?

Which region is underperforming?

Which products are contributing to the target gap?

Which customer segments generate the most revenue?

Which products have stronger margins?

Is regional performance improving year over year?

Where should management investigate first?

Project Objective

The objective is to demonstrate an end-to-end Business Intelligence workflow, from raw transactional data through data validation, analytical modeling, SQL analysis, statistical testing, visualization, root-cause investigation, and business recommendations.

The project emphasizes decision-oriented analytics rather than dashboard reporting alone.