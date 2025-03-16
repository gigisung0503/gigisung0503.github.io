---
title: "EDA and ETL Convention"
description: ""
author: "Gigi Sung"
date: "6/15/2024"
# draft: true
---



# Exploratory Data Analysis (EDA) 

>EDA should be a fun and liberal process 😇 but it's also important to have a structured approach to ensure a comprehensive understanding of the dataset. This template provides a systematic guide for conducting EDA and preparing the data for further analysis or modeling.





## 0. Mount Google Drive

First, you need to mount your Google Drive to the Colab environment. This will allow you to access files stored in your Google Drive.

```python
from google.colab import drive
drive.mount('/content/drive')
```

Running this code will prompt you to authorize access to your Google Drive. Follow the link provided, select your Google account, and copy the authorization code back into the Colab prompt.

## 0.1. Set Directory to a Specific Folder

Once your Google Drive is mounted, you can set the working directory to a specific folder within your Google Drive. For example, if you have a folder named `MyFolder` in your `MyDrive`, you can set the directory as follows:

```python
import os

# Set the directory to a specific folder in your Google Drive
os.chdir('/content/drive/MyDrive/MyFolder')

# Verify the current working directory
print(os.getcwd())
```

This code changes the current working directory to `MyFolder` within your Google Drive and prints the current working directory to confirm the change.


## 1. Data Loading and Initial Inspection

### 1.1 Import Libraries
Start by importing the necessary libraries for data manipulation and visualization.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

### 1.2 Load the Data
Load your dataset into a Pandas DataFrame.

```python
df = pd.read_csv('your_dataset.csv')
```

### 1.3 Initial Inspection
Inspect the first few rows, data types, and basic statistics.

```python
# Display the first few rows
print(df.head())

# Display data types and non-null counts
print(df.info())

# Display basic statistics
print(df.describe())
```

## 2. Data Cleaning and Preprocessing

### 2.1 Handling Missing Values
Identify and handle missing values.

```python
# Check for missing values
print(df.isnull().sum())

# Example: Fill missing values with the mean
df.fillna(df.mean(), inplace=True)
```

### 2.2 Handling Duplicates
Check for and remove duplicate rows.

```python
# Check for duplicates
print(df.duplicated().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)
```

### 2.3 Data Type Conversion
Convert data types if necessary.

```python
# Example: Convert a column to datetime
df['date_column'] = pd.to_datetime(df['date_column'])
```

### 2.4 Feature Engineering
Create new features if needed.

```python
# Example: Create a new feature from existing columns
df['new_feature'] = df['feature1'] / df['feature2']
```

## 3. Univariate, Bivariate, and Multivariate Analyses

### 3.1 Univariate Analysis
Analyze individual variables.

#### 3.1.1 Categorical Variables
Visualize the distribution of categorical variables.

```python
# Example: Bar plot for a categorical variable
sns.countplot(x='categorical_column', data=df)
plt.show()
```

#### 3.1.2 Numerical Variables
Visualize the distribution of numerical variables.

```python
# Example: Histogram for a numerical variable
sns.histplot(df['numerical_column'], kde=True)
plt.show()
```

### 3.2 Bivariate Analysis
Analyze relationships between two variables.

#### 3.2.1 Categorical vs. Numerical
Visualize the relationship between categorical and numerical variables.

```python
# Example: Box plot
sns.boxplot(x='categorical_column', y='numerical_column', data=df)
plt.show()
```

#### 3.2.2 Numerical vs. Numerical
Visualize the relationship between two numerical variables.

```python
# Example: Scatter plot
sns.scatterplot(x='numerical_column1', y='numerical_column2', data=df)
plt.show()
```

### 3.3 Multivariate Analysis
Analyze relationships between multiple variables.

#### 3.3.1 Correlation Matrix
Visualize the correlation between numerical variables.

```python
# Compute the correlation matrix
corr_matrix = df.corr()

# Plot the heatmap
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.show()
```

#### 3.3.2 Pair Plot
Visualize pairwise relationships in the dataset.

```python
# Pair plot
sns.pairplot(df)
plt.show()
```

## Conclusion
Summarize your findings and insights from the EDA. This structured approach ensures a comprehensive understanding of the dataset and prepares it for further analysis or modeling.



# ETL Convention

To construct an ETL (Extract, Transform, Load) pipeline, it's essential to follow a structured approach that ensures data is efficiently moved from source systems to a destination system, typically a data warehouse. Here is a detailed convention for building an ETL pipeline:

The following table shows the key libraries used in a typical Python-based ETL pipeline:


### Libraries Used

| Library       | Purpose                                      |
|---------------|----------------------------------------------|
| `pandas`      | Data manipulation and analysis               |
| `numpy`       | Numerical computing and array operations     |
| `requests`    | Making HTTP requests to APIs                 |
| `sqlalchemy`  | SQL toolkit and Object-Relational Mapping (ORM) |
| `airflow`     | Workflow management and scheduling           |
| `logging`     | Logging for monitoring and debugging         |
| `multiprocessing` | Parallel processing for performance optimization |

### 1. Setup and Import Libraries

```python
# Import necessary libraries
import pandas as pd
import numpy as np
import requests
from sqlalchemy import create_engine
import logging
from multiprocessing import Pool
```

### 2. Define ETL Functions

#### 2.1 Extract Data

```python
def extract_data_from_api(api_url):
    response = requests.get(api_url)
    data = response.json()
    df = pd.DataFrame(data)
    return df

def extract_data_from_db(connection_string, query):
    engine = create_engine(connection_string)
    df = pd.read_sql(query, con=engine)
    return df
```

#### 2.2 Transform Data

```python
def clean_data(df):
    df.dropna(inplace=True)  # Remove missing values
    df.drop_duplicates(inplace=True)  # Remove duplicates
    return df

def transform_data(df):
    df['date'] = pd.to_datetime(df['date'])  # Convert date column to datetime
    df['new_feature'] = df['feature1'] / df['feature2']  # Create a new feature
    return df
```

#### 2.3 Load Data

```python
def load_data_to_db(df, connection_string, table_name):
    engine = create_engine(connection_string)
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
```

### 3. Define the ETL Pipeline

```python
def etl_pipeline(api_url, db_connection_string, query, table_name):
    # Extract
    df_api = extract_data_from_api(api_url)
    df_db = extract_data_from_db(db_connection_string, query)
    
    # Transform
    df_api = clean_data(df_api)
    df_db = clean_data(df_db)
    df_api = transform_data(df_api)
    df_db = transform_data(df_db)
    
    # Load
    load_data_to_db(df_api, db_connection_string, table_name)
    load_data_to_db(df_db, db_connection_string, table_name)
```

### 4. Execute the ETL Pipeline

```python
# Define parameters
api_url = 'https://api.example.com/data'
db_connection_string = 'mysql+pymysql://user:password@host/dbname'
query = 'SELECT * FROM source_table'
table_name = 'destination_table'

# Run the ETL pipeline
etl_pipeline(api_url, db_connection_string, query, table_name)
```

### 5. Automate and Schedule the Pipeline

#### 5.1 Using Apache Airflow

```python
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

dag = DAG('etl_pipeline', default_args=default_args, schedule_interval='@daily')

extract_task = PythonOperator(task_id='extract', python_callable=extract_data_from_api, op_args=[api_url], dag=dag)
transform_task = PythonOperator(task_id='transform', python_callable=transform_data, op_args=[df], dag=dag)
load_task = PythonOperator(task_id='load', python_callable=load_data_to_db, op_args=[df, db_connection_string, table_name], dag=dag)

extract_task >> transform_task >> load_task
```

### 6. Logging and Error Handling

```python
logging.basicConfig(level=logging.INFO)

def etl_pipeline_with_logging(api_url, db_connection_string, query, table_name):
    try:
        logging.info('Starting ETL pipeline')
        
        # Extract
        df_api = extract_data_from_api(api_url)
        df_db = extract_data_from_db(db_connection_string, query)
        
        # Transform
        df_api = clean_data(df_api)
        df_db = clean_data(df_db)
        df_api = transform_data(df_api)
        df_db = transform_data(df_db)
        
        # Load
        load_data_to_db(df_api, db_connection_string, table_name)
        load_data_to_db(df_db, db_connection_string, table_name)
        
        logging.info('ETL pipeline completed successfully')
    except Exception as e:
        logging.error(f'Error in ETL pipeline: {e}')
```

### 7. Parallel Processing (Optional)

```python
def process_chunk(chunk):
    chunk = clean_data(chunk)
    chunk = transform_data(chunk)
    return chunk

def parallel_processing(df):
    chunks = [df[i:i+1000] for i in range(0, len(df), 1000)]
    with Pool(4) as p:
        processed_chunks = p.map(process_chunk, chunks)
    return pd.concat(processed_chunks)

# Example usage
df = parallel_processing(df)
```

By following this template, you can create a robust and efficient ETL pipeline using Python in a Jupyter Notebook. This template covers the essential steps of extracting, transforming, and loading data, along with automation, logging, and parallel processing for performance optimization.

