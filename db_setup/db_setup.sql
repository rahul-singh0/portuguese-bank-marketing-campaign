-- Create Database
CREATE DATABASE bank_campaign;

-- Set the Database
USE bank_campaign;

-- Create Table Schema
CREATE TABLE bank_marketing_campaign (
    age INT,
    job VARCHAR(50),
    marital VARCHAR(20),
    education VARCHAR(50),
    "default" VARCHAR(10),
    housing VARCHAR(10),
    loan VARCHAR(10),
    contact VARCHAR(10),
    month VARCHAR(10),
    day_of_week VARCHAR(10),
    duration INT,
    campaign INT,
    pdays INT,
    previous INT,
    poutcome VARCHAR(20),
    emp_var_rate FLOAT,
    cons_price_idx FLOAT,
    cons_conf_idx FLOAT,
    euribor3m FLOAT,
    nr_employed FLOAT,
    y VARCHAR(10)
);

-- Import Data from CSV (Change file path as required)
COPY bank_marketing_campaign
FROM '/Users/rahul/Documents/Analyst/Projects/Bank Marketing Campaign/dataset/bank-marketing.csv'
DELIMITER ','
CSV HEADER;