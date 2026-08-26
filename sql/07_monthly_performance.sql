-- Monthly sales performance and trend analysis
-- Completed orders only

WITH monthly AS (
    SELECT
        EXTRACT(YEAR FROM f.order_date)::INTEGER AS year,
        EXTRACT(MONTH FROM f.order_date)::INTEGER AS month_num,
        DATE_TRUNC('month', f.order_date)::DATE AS month,
        COUNT(DISTINCT f.order_id) AS orders,
        COUNT(DISTINCT f.customer_id) AS customers,
        SUM(f.net_sales) AS revenue,
        SUM(f.gross_margin) AS gross_margin,
        SUM(f.allocated_target) AS target
    FROM fact_sales f
    WHERE f.order_status = 'Completed'
    GROUP BY
        EXTRACT(YEAR FROM f.order_date),
        EXTRACT(MONTH FROM f.order_date),
        DATE_TRUNC('month', f.order_date)
)

SELECT
    year,
    month_num,
    TO_CHAR(month, 'YYYY-MM') AS month_label,
    orders,
    customers,
    revenue,
    gross_margin,
    target,
    ROUND(
        100.0 * revenue / NULLIF(target, 0),
        2
    ) AS attainment_pct,
    ROUND(
        100.0 * gross_margin / NULLIF(revenue, 0),
        2
    ) AS margin_pct,
    ROUND(
        revenue - target,
        2
    ) AS target_gap,
    ROUND(
        100.0 * (
            revenue / NULLIF(
                LAG(revenue) OVER (ORDER BY month),
                0
            ) - 1
        ),
        2
    ) AS mom_growth_pct
FROM monthly
ORDER BY month;