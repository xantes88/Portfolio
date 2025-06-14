
-- DROP TABLES IF EXISTS
DROP TABLE IF EXISTS invoices;
DROP TABLE IF EXISTS vendors;
DROP TABLE IF EXISTS payment_terms;
DROP TABLE IF EXISTS block_reasons;

-- CREATE VENDORS TABLE
CREATE TABLE vendors (
    vendor_id VARCHAR(10) PRIMARY KEY,
    vendor_name VARCHAR(100),
    region VARCHAR(20)
);

-- CREATE PAYMENT_TERMS TABLE
CREATE TABLE payment_terms (
    invoice_id INT PRIMARY KEY,
    payment_term VARCHAR(10)
);

-- CREATE BLOCK_REASONS TABLE
CREATE TABLE block_reasons (
    invoice_id INT PRIMARY KEY,
    block_reason VARCHAR(50)
);

-- CREATE INVOICES TABLE
CREATE TABLE invoices (
    invoice_id INT PRIMARY KEY,
    vendor_id VARCHAR(10),
    amount DECIMAL(10,2),
    due_in_days INT,
    rating INT,
    gl_code INT,
    invoice_date TIMESTAMP,
    due_date TIMESTAMP,
    payment_status VARCHAR(20),
    label INT,
    risk_score DECIMAL(5,4),
    FOREIGN KEY (vendor_id) REFERENCES vendors(vendor_id)
);

-- EXAMPLE INSERTS
-- Vendors
INSERT INTO vendors VALUES ('A001', 'Vendor IT', 'EMEA');
-- Payment Terms
INSERT INTO payment_terms VALUES (36, '60D');
-- Block Reasons
INSERT INTO block_reasons VALUES (36, 'none');
-- Invoices
INSERT INTO invoices VALUES (
    36, 'A001', 1763.00, 17, 2, 400300,
    '2025-03-16 14:33:10', '2025-04-30 14:33:10',
    'late', 1, 0.9839
);
