-- Regional and category performance
-- Used for root-cause drill-down

SELECT
    c.region,
    p.category,
    COUNT(DISTINCT f.order_id) AS orders,
    COUNT(DISTINCT f.customer_id) AS customers,
    SUM(f.units) AS units,
    SUM(f.net_sales) AS revenue,
    SUM(f.allocated_target) AS target,
    ROUND(
        100.0 * SUM(f.net_sales)
        / NULLIF(SUM(f.allocated_target), 0),
        2
    ) AS attainment_pct,
    ROUND(
        SUM(f.net_sales) - SUM(f.allocated_target),
        2
    ) AS target_gap,
    SUM(f.gross_margin) AS gross_margin,
    ROUND(
        100.0 * SUM(f.gross_margin)
        / NULLIF(SUM(f.net_sales), 0),
        2
    ) AS margin_pct
FROM fact_sales f
JOIN dim_customer c
    ON f.customer_id = c.customer_id
JOIN dim_product p
    ON f.product_name = p.product_name
WHERE f.order_status = 'Completed'
GROUP BY
    c.region,
    p.category
ORDER BY
    attainment_pct ASC;