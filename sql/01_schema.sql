-- ============================================================
-- Sales Performance, Customer & Revenue Intelligence Platform
-- PostgreSQL Analytical Schema
-- ============================================================

-- Customer dimension
CREATE TABLE dim_customer (
    customer_id VARCHAR(20) PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    segment VARCHAR(30) NOT NULL,
    region VARCHAR(30) NOT NULL,
    city VARCHAR(50),
    industry VARCHAR(80)
);

-- Product dimension
CREATE TABLE dim_product (
    product_name VARCHAR(100) PRIMARY KEY,
    category VARCHAR(50) NOT NULL,
    base_price NUMERIC(16,2),
    base_margin NUMERIC(8,4)
);

-- Region dimension
CREATE TABLE dim_region (
    region_key SERIAL PRIMARY KEY,
    region_name VARCHAR(30) UNIQUE NOT NULL
);

-- Date dimension
CREATE TABLE dim_date (
    date_key INTEGER PRIMARY KEY,
    full_date DATE UNIQUE NOT NULL,
    year INTEGER NOT NULL,
    quarter INTEGER NOT NULL,
    month INTEGER NOT NULL,
    month_name VARCHAR(20) NOT NULL
);

-- Sales fact
CREATE TABLE fact_sales (
    order_id VARCHAR(30) PRIMARY KEY,
    order_date DATE NOT NULL,
    customer_id VARCHAR(20) NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    region VARCHAR(30) NOT NULL,
    units INTEGER NOT NULL,
    gross_sales NUMERIC(16,2) NOT NULL,
    discount_pct NUMERIC(8,4) NOT NULL,
    net_sales NUMERIC(16,2) NOT NULL,
    gross_margin NUMERIC(16,2) NOT NULL,
    order_status VARCHAR(30) NOT NULL,
    salesperson VARCHAR(30),
    unit_price NUMERIC(16,4),
    cost NUMERIC(16,2),
    allocated_target NUMERIC(16,2),

    CONSTRAINT fk_customer
        FOREIGN KEY (customer_id)
        REFERENCES dim_customer(customer_id),

    CONSTRAINT fk_product
        FOREIGN KEY (product_name)
        REFERENCES dim_product(product_name)
);

-- Target fact
CREATE TABLE fact_targets (
    target_id SERIAL PRIMARY KEY,
    year INTEGER NOT NULL,
    region VARCHAR(30) NOT NULL,
    category VARCHAR(50) NOT NULL,
    target_sales NUMERIC(16,2) NOT NULL
);

-- Indexes
CREATE INDEX idx_fact_sales_date
    ON fact_sales(order_date);

CREATE INDEX idx_fact_sales_customer
    ON fact_sales(customer_id);

CREATE INDEX idx_fact_sales_product
    ON fact_sales(product_name);

CREATE INDEX idx_fact_sales_region
    ON fact_sales(region);