# Power BI Build Guide

## Data model
Use:
- FactSales
- DimCustomer
- DimProduct
- DimDate
- DimSalesperson (optional)

Relationships:
- FactSales[customer_id] -> DimCustomer[customer_id]
- FactSales[product_name] -> DimProduct[product_name]
- FactSales[order_date] -> DimDate[Date]

## Dashboard pages
1. Executive Overview: Revenue, margin, target attainment, monthly trend, regional contribution.
2. Regional Performance: region attainment, growth, margin and drill-down.
3. Product Performance: category/product revenue, units, margin and mix.
4. Customer Intelligence: customer contribution, segment performance and AOV.
5. Root Cause: region x category variance and drill-through.
6. Management Actions: prioritized recommendations supported by quantified evidence.

## QA
Reconcile Revenue, Customers, Orders and Target against SQL/Python outputs before publishing.
