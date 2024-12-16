# Portuguese Bank Marketing Campaign Insights & Analysis
<h1>Project Overview</h1>

<h3>Objective</h3>
<p>
    The objective of this project is to analyse the marketing campaigns of a Portuguese bank, focusing on understanding the factors influencing campaign success. By analysing various customer attributes and campaign outcomes, this project aims to uncover insights that can help improve future marketing strategies. The project involves exploring the dataset through data analysis and creating visualisations to interpret key patterns and trends.
</p>

<h3>Deliverables</h3>
<ul>
    <li>Data preparation, including data cleansing, validation, and transformation using Python and SQL.</li>
    <li>Exploratory Data Analysis (EDA), including visualisations that show the distribution of campaign success across different demographics, jobs, and months.</li>
    <li>Key insights and recommendations derived from analysing the relationship between customer attributes and campaign success.</li>
    <li>Creation of an interactive Power BI dashboard showcasing campaign performance metrics, trends, and key demographic insights.</li>
</ul>

<h3>Tools and Technologies Used</h3>
<ul>
    <li><b>PostgreSQL</b> for storing and managing the cleaned dataset.</li>
    <li><b>Python and SQL</b> for data cleansing and validation (libraries: Pandas, SQL queries).</li>
    <li><b>Python</b> for exploratory data analysis (EDA) and visualisation (libraries: Pandas, Matplotlib, Seaborn).</li>
    <li><b>Power BI</b> for creating interactive dashboards and visualisations.</li>
</ul>

<h1>Project Workflow</h1>
<h2>1. Define Scope and Metrics</h2>
<p>
    The first step of the project was to clearly define the scope and objectives. This involved understanding the problem at hand: predicting whether a customer would subscribe to a term deposit from a marketing campaign. The dataset provided various customer attributes (e.g., age, job, marital status) and campaign outcomes (e.g., whether they subscribed to the term deposit or not). 
</p>
<p>
    The key metric for the project was the binary outcome variable, `y`, which represents whether a customer subscribed to a term deposit ("yes" or "no"). Additionally, I focused on understanding which factors most influenced the likelihood of subscription, including customer demographics, economic conditions, and campaign attributes.
</p>
<h2>2. Data Preperation</h2>
<h3>2.1 Database Creation and Set Up</h3>

<p>I created a new database called bank_campaign and defined the schema for the bank_marketing_campaign table, aligning it with the dataset’s structure. After setting up the schema, I imported the data using the COPY command, loading the CSV file into the database for analysis.</p>

```sql
CREATE DATABASE bank_campaign;
```

```sql
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
```

```sql
COPY bank_marketing_campaign
FROM '/Users/rahul/Documents/Analyst/Projects/Bank Marketing Campaign/dataset/bank-marketing.csv'
DELIMITER ','
CSV HEADER;
```

<h3>2.2 Data Cleansing</h3>

<p>I cleaned the data by removing invalid records with negative values in key fields, checking and removing duplicates, and standardising the case of categorical values. Additionally, I used Python to identify missing values, duplicate rows, and leading or trailing spaces in categorical columns, ensuring the dataset was clean and ready for analysis.</p>

<h4>Removing Invalid Data</h4>

```sql
DELETE FROM bank_marketing_campaign 
WHERE age < 0 OR duration < 0;
```
<h4>Checking for Duplicates</h4>

```sql
SELECT age, job, marital, education, default, housing, loan, contact, month, day_of_week, duration, campaign, pdays, previous, emp_var_rate, cons_price_idx, cons_conf_idx, euribor3m, nr_employed, y, COUNT(*) 
FROM bank_marketing_campaign
GROUP BY age, job, marital, education, default, housing, loan, contact, month, day_of_week, duration, campaign, pdays, previous, emp_var_rate, cons_price_idx, cons_conf_idx, euribor3m, nr_employed, y
HAVING COUNT(*) > 1;

DELETE FROM bank_marketing_campaign
WHERE ctid NOT IN (SELECT MIN(ctid)
                    FROM bank_marketing_campaign
                    GROUP BY age, job, marital, education, default, housing, loan, contact, month, day_of_week, duration, campaign, pdays, previous, emp_var_rate, cons_price_idx, cons_conf_idx, euribor3m, nr_employed, y);
```

<h4>Updating Inconsistent Values</h4>

```sql
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
```

<h4>Validating and Further Cleansing Data with Python</h4>

```python
# SQL query to fetch all data from the cleaned table
query = "SELECT * FROM bank_marketing_campaign"

# Load the cleaned data into a pandas DataFrame
df = pd.read_sql(query, engine)
print(df.head())

# Check for missing values in the dataset
missing_values = df.isnull().sum()
print(missing_values)

# Check for duplicates
duplicates = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")

# List of all categorical columns in the dataset
categorical_columns = ['job', 'education', 'marital', 'default', 'housing', 'loan', 
                       'contact', 'month', 'day_of_week', 'poutcome', 'y']

# Check for unique values in each categorical column
for column in categorical_columns:
    print(f"Unique values in {column}: {df[column].unique()}")

# Check for leading or trailing spaces in all categorical columns
rows_with_spaces = df[categorical_columns].apply(lambda x: x.str.strip() != x).any(axis=1)

# Display rows with leading or trailing spaces
print(df[rows_with_spaces])
```

<h2>3. Exploratory Data Analysis</h2>
<h2>4. Data Visualisation</h2>
