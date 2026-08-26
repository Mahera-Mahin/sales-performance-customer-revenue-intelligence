-- ============================================================
-- Executive KPI
-- ============================================================

SELECT
    COUNT(*) AS completed_orders,
    COUNT(DISTINCT customer_id) AS active_customers,
    ROUND(SUM(net_sales), 2) AS revenue,
    ROUND(SUM(gross_margin), 2) AS gross_margin,
    ROUND(
        SUM(gross_margin)
        / NULLIF(SUM(net_sales), 0) * 100,
        2
    ) AS margin_pct,
    ROUND(AVG(net_sales), 2) AS avg_order_value
FROM fact_sales
WHERE order_status = 'Completed';


-- ============================================================
-- Regional Performance
-- ============================================================

SELECT
    region,
    COUNT(*) AS orders,
    COUNT(DISTINCT customer_id) AS customers,
    ROUND(SUM(net_sales), 2) AS revenue,
    ROUND(SUM(gross_margin), 2) AS gross_margin,
    ROUND(
        SUM(gross_margin)
        / NULLIF(SUM(net_sales), 0) * 100,
        2
    ) AS margin_pct
FROM fact_sales
WHERE order_status = 'Completed'
GROUP BY region
ORDER BY revenue DESC;


-- ============================================================
-- Customer Segment Performance
-- ============================================================

SELECT
    c.segment,
    COUNT(DISTINCT f.customer_id) AS customers,
    COUNT(*) AS orders,
    ROUND(SUM(f.net_sales), 2) AS revenue,
    ROUND(
        SUM(f.net_sales)
        / NULLIF(COUNT(DISTINCT f.customer_id), 0),
        2
    ) AS revenue_per_customer
FROM fact_sales f
JOIN dim_customer c
    ON f.customer_id = c.customer_id
WHERE f.order_status = 'Completed'
GROUP BY c.segment
ORDER BY revenue DESC;


-- ============================================================
-- Product Performance
-- ============================================================

SELECT
    p.category,
    p.product_name,
    COUNT(*) AS orders,
    SUM(f.units) AS units,
    ROUND(SUM(f.net_sales), 2) AS revenue,
    ROUND(SUM(f.gross_margin), 2) AS gross_margin,
    ROUND(
        SUM(f.gross_margin)
        / NULLIF(SUM(f.net_sales), 0) * 100,
        2
    ) AS margin_pct
FROM fact_sales f
JOIN dim_product p
    ON f.product_name = p.product_name
WHERE f.order_status = 'Completed'
GROUP BY
    p.category,
    p.product_name
ORDER BY revenue DESC;


-- ============================================================
-- Top Customers
-- ============================================================

SELECT
    c.customer_id,
    c.customer_name,
    c.segment,
    c.industry,
    c.region,
    c.city,
    COUNT(*) AS orders,
    ROUND(SUM(f.net_sales), 2) AS revenue,
    ROUND(SUM(f.gross_margin), 2) AS gross_margin
FROM fact_sales f
JOIN dim_customer c
    ON f.customer_id = c.customer_id
WHERE f.order_status = 'Completed'
GROUP BY
    c.customer_id,
    c.customer_name,
    c.segment,
    c.industry,
    c.region,
    c.city
ORDER BY revenue DESC
LIMIT 25;