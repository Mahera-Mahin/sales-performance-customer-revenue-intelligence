-- Customer performance analysis
-- Completed orders only

SELECT
    c.customer_id,
    c.customer_name,
    c.segment,
    c.region,
    c.industry,
    COUNT(DISTINCT f.order_id) AS orders,
    SUM(f.units) AS units,
    SUM(f.net_sales) AS revenue,
    SUM(f.gross_margin) AS gross_margin,
    ROUND(
        100.0 * SUM(f.gross_margin)
        / NULLIF(SUM(f.net_sales), 0),
        2
    ) AS margin_pct,
    ROUND(
        SUM(f.net_sales)
        / NULLIF(COUNT(DISTINCT f.order_id), 0),
        2
    ) AS avg_order_value
FROM fact_sales f
JOIN dim_customer c
    ON f.customer_id = c.customer_id
WHERE f.order_status = 'Completed'
GROUP BY
    c.customer_id,
    c.customer_name,
    c.segment,
    c.region,
    c.industry
ORDER BY revenue DESC;