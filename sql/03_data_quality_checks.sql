-- ============================================================
-- Data Quality Checks
-- Expected result: zero failures
-- ============================================================

-- Null customer keys
SELECT COUNT(*) AS null_customer_keys
FROM fact_sales
WHERE customer_id IS NULL;


-- Null product keys
SELECT COUNT(*) AS null_product_keys
FROM fact_sales
WHERE product_name IS NULL;


-- Negative sales
SELECT COUNT(*) AS invalid_sales
FROM fact_sales
WHERE net_sales < 0;


-- Invalid units
SELECT COUNT(*) AS invalid_units
FROM fact_sales
WHERE units <= 0;


-- Invalid discounts
SELECT COUNT(*) AS invalid_discount
FROM fact_sales
WHERE discount_pct < 0
   OR discount_pct > 1;


-- Duplicate order IDs
SELECT
    order_id,
    COUNT(*) AS duplicate_count
FROM fact_sales
GROUP BY order_id
HAVING COUNT(*) > 1;


-- Margin reconciliation
SELECT COUNT(*) AS margin_mismatches
FROM fact_sales
WHERE ABS(
    gross_margin - (net_sales - cost)
) > 0.01;


-- Missing order dates
SELECT COUNT(*) AS null_order_dates
FROM fact_sales
WHERE order_date IS NULL;


-- Invalid order status
SELECT COUNT(*) AS invalid_status
FROM fact_sales
WHERE order_status NOT IN ('Completed', 'Returned');