-- Product performance analysis
-- Completed orders only

SELECT
    p.category,
    p.product_name,
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
        / NULLIF(SUM(f.units), 0),
        2
    ) AS revenue_per_unit
FROM fact_sales f
JOIN dim_product p
    ON f.product_name = p.product_name
WHERE f.order_status = 'Completed'
GROUP BY
    p.category,
    p.product_name
ORDER BY revenue DESC;