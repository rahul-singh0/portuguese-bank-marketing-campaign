-- Remove Invalid Data
DELETE FROM bank_marketing_campaign 
WHERE age < 0 OR duration < 0;

-- Check and Remove Duplicates
SELECT age, job, marital, education, default, housing, loan, contact, month, day_of_week, duration, campaign, pdays, previous, emp_var_rate, cons_price_idx, cons_conf_idx, euribor3m, nr_employed, y, COUNT(*) 
FROM bank_marketing_campaign
GROUP BY age, job, marital, education, default, housing, loan, contact, month, day_of_week, duration, campaign, pdays, previous, emp_var_rate, cons_price_idx, cons_conf_idx, euribor3m, nr_employed, y
HAVING COUNT(*) > 1;

DELETE FROM bank_marketing_campaign
WHERE ctid NOT IN (SELECT MIN(ctid)
                    FROM bank_marketing_campaign
                    GROUP BY age, job, marital, education, default, housing, loan, contact, month, day_of_week, duration, campaign, pdays, previous, emp_var_rate, cons_price_idx, cons_conf_idx, euribor3m, nr_employed, y);

-- Update Inconsistent Values
UPDATE bank_marketing_campaign
SET
    emp_var_rate = ROUND(emp_var_rate::numeric, 2),
    cons_price_idx = ROUND(cons_price_idx::numeric, 2),
    cons_conf_idx = ROUND(cons_conf_idx::numeric, 2),
    euribor3m = ROUND(euribor3m::numeric, 2),
    nr_employed = ROUND(nr_employed::numeric, 2),
    marital = LOWER(marital),
    education = LOWER(education),
    "default" = LOWER("default"),
    housing = LOWER(housing),
    loan = LOWER(loan),
    contact = LOWER(contact),
    month = LOWER(month),
    day_of_week = LOWER(day_of_week),
    poutcome = LOWER(poutcome),
    y = LOWER(y);

-- Check for Missing or Null Values and Remove or Replace
DELETE FROM bank_marketing_campaign
WHERE age IS NULL OR job IS NULL OR y IS NULL;