# Power BI DAX Measures

Build a star schema with FactSales -> DimCustomer, DimProduct and DimDate.

```DAX
Revenue =
CALCULATE(SUM(FactSales[net_sales]), FactSales[order_status] = "Completed")

Gross Margin =
CALCULATE(SUM(FactSales[gross_margin]), FactSales[order_status] = "Completed")

Margin % = DIVIDE([Gross Margin], [Revenue])

Orders =
CALCULATE(DISTINCTCOUNT(FactSales[order_id]), FactSales[order_status] = "Completed")

Customers =
CALCULATE(DISTINCTCOUNT(FactSales[customer_id]), FactSales[order_status] = "Completed")

Average Order Value = DIVIDE([Revenue], [Orders])

Target =
CALCULATE(SUM(FactSales[allocated_target]), FactSales[order_status] = "Completed")

Target Attainment % = DIVIDE([Revenue], [Target])

Target Variance = [Revenue] - [Target]

Revenue YoY % =
VAR PriorYear = CALCULATE([Revenue], SAMEPERIODLASTYEAR('Date'[Date]))
RETURN DIVIDE([Revenue] - PriorYear, PriorYear)
```
