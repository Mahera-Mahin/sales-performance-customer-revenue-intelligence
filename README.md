# Sales Performance, Customer & Revenue Intelligence Platform

A Business Intelligence and analytics solution that transforms transactional sales data into **validated KPIs, performance insights, root-cause analysis, and interactive Power BI reporting**.

**Tech Stack:** SQL · PostgreSQL · Python · Pandas · NumPy · SciPy · Power BI · DAX · Power Query · PyTest · Git/GitHub

> **Data Note:** Synthetic dataset created specifically for portfolio analysis.

---

## 📊 Project at a Glance

| **Metric** | **Result** |
|---|---:|
| Transactions | 50,000 |
| Customers | 2,200 |
| Regions | 5 |
| Products / Product Families | 8 |
| Analysis Period | 2023–2025 |
| Completed Orders | 47,017 |
| Revenue | ₹8.67B |
| Gross Margin | ₹1.83B |
| Gross Margin % | 21.16% |
| Target Attainment | 97.51% |
| Average Order Value | ₹184,334 |

---

## 🎯 Business Objective

Build a decision-oriented BI platform to answer:

- Are sales targets being achieved?
- Which regions and products drive revenue and margin?
- Which customers and segments contribute the most value?
- Where are the largest performance gaps?
- What factors contribute to underperformance?
- How is performance changing over time?

---

## 🔄 Analytical Workflow

```text
Raw Sales Data
      ↓
Data Quality Validation
      ↓
SQL / PostgreSQL Analysis
      ↓
Python EDA & Statistical Analysis
      ↓
Power BI / DAX Reporting
      ↓
Root-Cause Analysis
📈 Power BI Dashboard

Five interactive dashboard pages were developed:

Executive Overview — Revenue, gross margin, target attainment, customers, monthly trends and regional performance.
Regional Performance — Revenue vs target, target attainment, margin, variance and regional trends.
Product Performance — Product/category revenue, units, margin and target performance.
Customer Intelligence — Customer contribution, segments, and top customers.
Root Cause Analysis — Region → Category → Product drill-down to identify performance gaps.
Dashboard Screenshots

Executive Overview

Regional Performance

Product Performance

Customer Intelligence

Root Cause Analysis

🔍 Key Analytical Work
Built reusable SQL queries for executive KPIs, customer, product, regional and monthly performance.
Developed Python workflows for data validation, KPI generation, EDA and root-cause analysis.
Implemented automated checks for duplicates, missing values, invalid sales/discounts, units and margin reconciliation.
Applied one-way ANOVA to evaluate order-value differences across customer segments.
Developed DAX measures for Revenue, Gross Margin, Margin %, Target Attainment, Target Variance, AOV and YoY analysis.
Performed hierarchical Region → Category → Product analysis to investigate target gaps.
Example Finding

East → Engines → Industrial Engines | 2025

Metric	Result
Revenue	₹116.54M
Target	₹125.14M
Target Attainment	93.13%
Target Gap	-₹8.60M
Margin	15.84%
🛠️ Technical Implementation
Data & Analytics

Python · Pandas · NumPy · SciPy · Exploratory Data Analysis · Statistical Analysis · Root-Cause Analysis

SQL & Database

SQL · PostgreSQL · KPI Queries · Data-Quality Checks · Analytical Data Modeling

Business Intelligence

Power BI · DAX · Power Query · KPI Dashboards · Trend & Variance Analysis · Interactive Filtering · Drill-Down

Quality & Development

PyTest · Git · GitHub

📁 Repository Structure
├── data/
│   ├── raw/
│   └── processed/
├── sql/
├── src/
├── powerbi/
├── docs/
│   └── dashboard/
├── tests/
├── requirements.txt
└── README.md
▶️ Run the Analysis
pip install -r requirements.txt

python src/01_data_quality.py
python src/02_eda_and_kpis.py
python src/03_hypothesis_testing.py
python src/04_root_cause_analysis.py

pytest
💡 Business Questions Supported
Area	Question
Performance	Are we achieving targets?
Regional	Which regions are driving or missing targets?
Product	Which products contribute to revenue and margin?
Customer	Which customers and segments drive value?
Diagnostic	Where are the largest performance gaps?
Trend	How are revenue and performance changing over time?
📌 Outcome

A complete BI workflow connecting data quality → SQL analytics → Python analysis → statistical validation → Power BI reporting → root-cause investigation, demonstrating practical capabilities in Business Intelligence, data analysis, KPI reporting, and decision support.

Data Disclaimer

This repository uses synthetic data created for portfolio purposes. All metrics and business findings apply only to this dataset.


**This is the version I would commit.** It is concise enough for a recruiter to scan quickly while still showing t
