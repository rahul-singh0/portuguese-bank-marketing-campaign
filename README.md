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

<p>
    After the data was cleaned, exploratory data analysis (EDA) was performed to understand trends, distributions, and correlations in the dataset. Key tasks included:
</p>
<ul>
    <li>Examining individual features like age, job type, and campaign success to understand their distribution.</li>
    <li>Investigating relationships between features such as the correlation between `age` and `y` (campaign success), or `job` and `y`.</li>
    <li>Using bar charts, histograms, and box plots to visualise distributions and relationships between features. For example, visualising how campaign success varies by job type or age group.</li>
</ul>
<p>
    The goal of EDA was to uncover patterns and provide a deeper understanding of the dataset that could inform the creation of the final dashboard and key insights and recommendations.
</p>

<p>Below are a couple examples of visualisations from the EDA. You can find all the visualisations along with the corresponding source code here.</p>

<h4>Age Distribution of Customers</h4>
<p>
    This histogram shows the distribution of customer ages. The peak is around the 30-40 age range, which is valuable for identifying the core customer demographic.
</p>

```python
## 1.1. Plot the distribution of 'age'
plt.figure(figsize=(8, 6))
sns.histplot(df['age'], kde=True, bins=30)
plt.title('Age Distribution of Customers')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
```

![age_distribution](https://github.com/user-attachments/assets/61d064f6-83dd-4649-a356-763e73e51a02)


<h4>Consumer Confidence Index vs. Campaign Success</h4>
<p>
    This box plot reveals how campaigns performed based on the Consumer Confidence Index (CCI). It indicates that campaigns are generally more successful when consumer confidence is higher.
</p>

```python
## 3.3. Explore the relationship between 'cons_conf_idx' and campaign success
plt.figure(figsize=(8, 6))
sns.boxplot(x='y', y='cons_conf_idx', data=df)
plt.title('Consumer Confidence Index vs. Campaign Success')
plt.xlabel('Campaign Success')
plt.ylabel('Consumer Confidence Index')  # Descriptive y-axis label
plt.show()
```

![cci_campaign_success](https://github.com/user-attachments/assets/1614a06e-5af0-4e63-9158-53242b164e72)



<h3>Key Findings from the EDA</h3>
<ul>
    <li><b>Demographics:</b> The majority of customers are between 30-40 years old, suggesting a primary target market for campaigns.</li>
    <li><b>Campaign Duration:</b> Most campaigns are brief, and shorter campaigns tend to have higher success rates.</li>
    <li><b>Economic Factors:</b> The Consumer Confidence Index (CCI) and Employment Variation Rate are significant factors that impact campaign success.</li>
    <li><b>Customer Segmentation:</b> The dataset shows a wide range of job types, with "admin" and "technician" being the most common, helping to tailor customer segmentation strategies.</li>
</ul>


<h2>4. Data Visualisation</h2>

<p>
    The final stage of the project involved creating an interactive Power BI dashboard to communicate the insights derived from the analysis. The dashboard was designed to be user-friendly, allowing users to explore various aspects of the marketing campaign's success. Key features of the dashboard included:
</p>
<ul>
    <li><b>Campaign performance:</b> Displaying the total number of successful term deposit sign-ups, and how success varied by demographics, job types, and months.</li>
    <li><b>Trend analysis:</b> Showing how campaign success changed over time, such as by month and day of the week.</li>
    <li><b>Interactivity:</b> Incorporating slicers for demographics, job types, and months, allowing users to filter and explore the data from different angles.</li>
    <li><b>Key insights:</b> Displaying insights based on the EDA phase, such as which job types had the highest success rates and which months saw more conversions.</li>
</ul>

https://github.com/user-attachments/assets/2da8dfec-d660-4e9e-a331-6fa1d2873858

<h2>Conclusion</h2>

<p>
    The project provided valuable insights into the performance of a marketing campaign for a Portuguese bank, focusing on customer characteristics and campaign success. By leveraging exploratory data analysis (EDA) and data visualisation techniques, several key patterns were uncovered that could inform future marketing strategies.
</p>

<h3>Key Insights</h3>
<ul>
    <li><b>Age Distribution of Customers:</b> The analysis revealed that the majority of customers fall within the 30-40 age range, which represents the bank's core demographic. Understanding this age group can help the bank tailor marketing efforts to better engage this audience.</li>
    <li><b>Consumer Confidence Index (CCI):</b> Campaigns were more successful when the consumer confidence index was higher. This suggests that economic conditions, particularly consumer confidence, play a significant role in the likelihood of campaign success. The bank could monitor CCI trends to optimise campaign timing and messaging.</li>
    <li><b>Campaign Duration:</b> The distribution of campaign durations showed a heavy concentration of short-duration calls, which could indicate either a low-effort approach or the use of multiple contacts to engage potential customers. This may imply that longer interactions are needed to improve success rates.</li>
    <li><b>Employment Variation Rate:</b> A higher employment variation rate was correlated with successful campaigns, suggesting that the economic environment or employment trends may influence the success of marketing campaigns. The bank could incorporate external economic indicators like employment rates into their campaign strategy to target more receptive segments.</li>
    <li><b>Contact Method:</b> The majority of campaigns were conducted via mobile phones (cellular), highlighting the importance of digital outreach in reaching potential customers. It is crucial for the bank to continue optimising their digital communication channels.</li>
</ul>

<h3>Recommendations</h3>
<ul>
    <li><b>Targeting Specific Age Groups:</b> Given that the core customer base is concentrated in the 30-40 age range, the bank should consider creating targeted campaigns for this group, particularly those offering age-appropriate financial products.</li>
    <li><b>Adapt Campaigns to Economic Indicators:</b> The positive relationship between consumer confidence and campaign success suggests that the bank should track and respond to economic indicators like CCI and employment variation to time and target campaigns more effectively.</li>
    <li><b>Optimise Campaign Durations:</b> Since shorter calls dominate, further analysis on the effectiveness of call length is recommended. It may be beneficial to experiment with longer, more personalised campaigns that can improve conversion rates.</li>
    <li><b>Leverage Digital Channels:</b> Given the success of mobile communication, the bank should continue investing in digital outreach and explore newer technologies like mobile apps or automated SMS to engage with customers more efficiently.</li>
    <li><b>Further Segmentation:</b> A more granular segmentation of the customer base based on additional factors like income, education, and loan status could uncover more specific insights, allowing the bank to fine-tune its marketing strategies even further.</li>
</ul>

<p>
    By incorporating these insights and recommendations, the bank can improve its marketing effectiveness, maximise campaign success rates, and ensure that resources are optimally allocated to engage the most promising customer segments.
</p> 


