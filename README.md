# Sales Performance, Customer & Revenue Intelligence Platform

A portfolio-grade Business Intelligence case study demonstrating **sales reporting, KPI analytics, data quality, customer intelligence, root-cause analysis, statistical testing and executive decision support**.

> **Dataset:** reproducible synthetic sales data created specifically for this portfolio project. It is not Cummins data and does not represent actual Cummins performance.

## Business workflow

**Raw transactions → data quality → SQL → analytical model → Power BI KPIs → trend/variance analysis → root cause → hypothesis testing → management recommendations**

## Dataset
- 50,000 transactions
- 2,200 customers
- 5 regions
- 8 products/product families
- 2023–2025
- Revenue, cost, margin, discount and target fields

## Technology
**SQL · Power BI · Excel · Python · Pandas · DAX · Power Query · Git**

## Repository
```text
├── data/
├── sql/
├── src/
├── powerbi/
├── docs/
└── tests/
```

## Run
```bash
pip install -r requirements.txt
python src/01_data_quality.py
python src/02_eda_and_kpis.py
python src/03_hypothesis_testing.py
```

## Power BI
Use `powerbi/BUILD_GUIDE.md` and `powerbi/DAX_Measures.md`.

## Disclaimer
Independent portfolio project using synthetic data. Not affiliated with or endorsed by Cummins.
