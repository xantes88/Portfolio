CREATE TABLE invoices_enhanced (
    invoice_id INT,
    vendor_id VARCHAR(255),
    amount INT,
    due_in_days INT,
    rating INT,
    gl_code INT,
    invoice_date TIMESTAMP,
    due_date TIMESTAMP,
    payment_status VARCHAR(255),
    label INT,
    is_overdue INT,
    urgency_score FLOAT,
    high_risk_vendor INT,
    invoice_age INT,
    due_weekday INT,
    due_month INT,
    due_month_end_flag INT,
    due_quarter INT,
    vendor_avg_delay FLOAT,
    vendor_late_rate FLOAT,
    vendor_recent_risk FLOAT,
    category_econ_index FLOAT,
    vendor_avg_discount FLOAT,
    invoice_month VARCHAR(255),
    vendor_monthly_volume INT,
    category_IT BOOLEAN,
    category_Logistics BOOLEAN,
    category_Maintenance BOOLEAN,
    category_Office Supplies BOOLEAN,
    company_code_C002 BOOLEAN,
    company_code_C003 BOOLEAN,
    vendor_region_APAC BOOLEAN,
    vendor_region_EMEA BOOLEAN,
    payment_term_45D BOOLEAN,
    payment_term_60D BOOLEAN,
    block_reason_missing PO BOOLEAN,
    block_reason_none BOOLEAN,
    block_reason_price mismatch BOOLEAN,
    risk_score FLOAT,
    vendor_name VARCHAR(255)
);


-- 1. Late invoice ratio per vendor
SELECT vendor_name,
       COUNT(*) AS total_invoices,
       SUM(CASE WHEN payment_status = 'late' THEN 1 ELSE 0 END) AS late_invoices,
       ROUND(SUM(CASE WHEN payment_status = 'late' THEN 1.0 ELSE 0 END) / COUNT(*), 2) AS late_ratio
FROM invoices_enhanced
GROUP BY vendor_name
ORDER BY late_ratio DESC;

-- 2. Average invoice amount by payment term
SELECT payment_term_45D, payment_term_60D,
       AVG(amount) AS avg_amount
FROM invoices_enhanced
GROUP BY payment_term_45D, payment_term_60D;

-- 3. Risk score distribution
SELECT 
    CASE 
        WHEN risk_score >= 0.8 THEN 'High Risk'
        WHEN risk_score >= 0.5 THEN 'Medium Risk'
        ELSE 'Low Risk'
    END AS risk_level,
    COUNT(*) AS count
FROM invoices_enhanced
GROUP BY risk_level;

-- 4. Invoices by region and status
SELECT 
    CASE 
        WHEN vendor_region_APAC THEN 'APAC'
        WHEN vendor_region_EMEA THEN 'EMEA'
        ELSE 'OTHER'
    END AS region,
    payment_status,
    COUNT(*) AS total
FROM invoices_enhanced
GROUP BY region, payment_status;
