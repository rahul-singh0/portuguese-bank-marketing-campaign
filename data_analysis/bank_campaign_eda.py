import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# Define Database
database_url = 'postgresql://postgres@localhost:5432/bank_campaign_data'

# Create the connection engine
engine = create_engine(database_url)

# Load the data from the database
df = pd.read_sql("SELECT * FROM bank_marketing_campaign", engine)

# Map education values to more meaningful labels
education_mapping = {
    'basic.9y': 'Primary Education (9 years)',
    'basic.4y': 'Basic Education (4 years)',
    'basic.6y': 'Primary Education (6 years)',
    'university.degree': 'University Degree',
    'high.school': 'High School',
    'professional.course': 'Professional Course',
    'basic.4y': 'Basic Education (4 years)',
    'basic.6y': 'Basic Education (6 years)',
    'unknown': 'Unknown',
    'illiterate': 'Illiterate'
}

# Apply the mapping to the 'education' column
df['education'] = df['education'].map(education_mapping)

# Set the style for the plots
sns.set(style="whitegrid")

# 1. Analyze Demographics

## 1.1. Plot the distribution of 'age'
plt.figure(figsize=(8, 6))
sns.histplot(df['age'], kde=True, bins=30)
plt.title('Age Distribution of Customers')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

## 1.2. Plot the distribution of 'job'
plt.figure(figsize=(10, 6))
sns.countplot(y=df['job'], order=df['job'].value_counts().index)
plt.title('Distribution of Customer Jobs')
plt.xlabel('Frequency')
plt.ylabel('Job')
plt.show()

## 1.3. Plot the distribution of 'education'
plt.figure(figsize=(8, 6))
sns.countplot(x=df['education'], order=df['education'].value_counts().index)
plt.title('Distribution of Customer Education Levels')
plt.xlabel('Education Level')
plt.ylabel('Frequency')
plt.show()

## 1.4. Plot the distribution of 'marital'
plt.figure(figsize=(8, 6))
sns.countplot(x=df['marital'], order=df['marital'].value_counts().index)
plt.title('Distribution of Customer Marital Status')
plt.xlabel('Marital Status')
plt.ylabel('Frequency')
plt.show()

# 2. Campaign Analysis

## 2.1. Plot the distribution of 'contact' method
plt.figure(figsize=(8, 6))
sns.countplot(x=df['contact'], order=df['contact'].value_counts().index)
plt.title('Contact Method Distribution')
plt.xlabel('Contact Method')
plt.ylabel('Frequency')
plt.show()

## 2.2. Plot the distribution of 'duration'
plt.figure(figsize=(8, 6))
sns.histplot(df['duration'], kde=True, bins=30)
plt.title('Campaign Duration Distribution')
plt.xlabel('Duration (in seconds)')
plt.ylabel('Frequency')
plt.show()

## 2.3. Plot the distribution of 'previous' contacts
plt.figure(figsize=(8, 6))
sns.histplot(df['previous'], kde=True, bins=30)
plt.title('Previous Contacts Distribution')
plt.xlabel('Previous Contacts')
plt.ylabel('Frequency')
plt.show()

# 3. Economic Trends Analysis

## 3.1. Explore the relationship between 'emp_var_rate' and campaign success
plt.figure(figsize=(8, 6))
sns.boxplot(x='y', y='emp_var_rate', data=df)
plt.title('Employment Variation Rate vs. Campaign Success')
plt.xlabel('Campaign Success')
plt.ylabel('Employment Variation Rate (%)')  # Descriptive y-axis label
plt.show()

## 3.2. Explore the relationship between 'cons_price_idx' and campaign success
plt.figure(figsize=(8, 6))
sns.boxplot(x='y', y='cons_price_idx', data=df)
plt.title('Consumer Price Index (CPI) vs. Campaign Success')
plt.xlabel('Campaign Success')
plt.ylabel('Consumer Price Index (CPI)')  # Descriptive y-axis label
plt.show()

## 3.3. Explore the relationship between 'cons_conf_idx' and campaign success
plt.figure(figsize=(8, 6))
sns.boxplot(x='y', y='cons_conf_idx', data=df)
plt.title('Consumer Confidence Index vs. Campaign Success')
plt.xlabel('Campaign Success')
plt.ylabel('Consumer Confidence Index')  # Descriptive y-axis label
plt.show()

## 3.4. Explore the relationship between 'euribor3m' and campaign success
plt.figure(figsize=(8, 6))
sns.boxplot(x='y', y='euribor3m', data=df)
plt.title('Euribor 3-Month Rate vs. Campaign Success')
plt.xlabel('Campaign Success')
plt.ylabel('Euribor 3-Month Rate (%)')  # Descriptive y-axis label
plt.show()

## 3.5. Explore the relationship between 'nr_employed' and campaign success
plt.figure(figsize=(8, 6))
sns.boxplot(x='y', y='nr_employed', data=df)
plt.title('Number of Employees vs. Campaign Success')
plt.xlabel('Campaign Success')
plt.ylabel('Number of Employees (in millions)')  # Descriptive y-axis label
plt.show()