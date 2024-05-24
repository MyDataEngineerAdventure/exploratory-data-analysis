#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import pyspark.sql.types as T
from pyspark.sql import DataFrame

# Start Spark session
spark = SparkSession.builder.appName("CDC Example").getOrCreate()

# Define schema
schema = T.StructType([
    T.StructField("id", T.IntegerType(), True),
    T.StructField("name", T.StringType(), True),
    T.StructField("age", T.IntegerType(), True),
    T.StructField("salary", T.IntegerType(), True)
])

# Data for old DataFrame
data_old = [
    (1, "Alice", 30, 5000),
    (2, "Bob", 34, 5500),
    (3, "Charlie", 28, 6000),
    (4, "David", 45, 6200)
]

# Data for new DataFrame
data_new = [
    (1, "Alice", 30, 5000),  # No change
    (2, "Bob", 35, 5500),    # Updated age
    (3, "Charlie", 28, 6100), # Updated salary
    (5, "Eve", 23, 4800)     # New record
]

# Create DataFrames
df_old = spark.createDataFrame(data_old, schema=schema)
df_new = spark.createDataFrame(data_new, schema=schema)

# Register as views for Spark SQL usage
df_old.createOrReplaceTempView("df_old")
df_new.createOrReplaceTempView("df_new")


# In[2]:


df_old.show()


# In[3]:


df_new.show()


# In[4]:


def perform_cdc(df_old: DataFrame, df_new: DataFrame, join_keys: list, compare_columns: list, old_name: str, new_name: str) -> DataFrame:
    # Register DataFrames as temporary views
    df_old.createOrReplaceTempView("df_old")
    df_new.createOrReplaceTempView("df_new")
    
    # Prepare SQL conditions
    join_condition = " AND ".join([f"new.{key} = old.{key}" for key in join_keys])
    compare_condition = " AND ".join([f"new.{col} = old.{col}" for col in compare_columns])
    
    # SQL queries for different change types
    inserts_sql = f"""
    SELECT new.*, 'Insert' as Change_Type, '{new_name}' as New_DF, '{old_name}' as Old_DF
    FROM df_new new
    LEFT JOIN df_old old ON {join_condition}
    WHERE old.{join_keys[0]} IS NULL
    """
    
    updates_sql = f"""
    SELECT new.*, 'Update' as Change_Type, '{new_name}' as New_DF, '{old_name}' as Old_DF
    FROM df_new new
    JOIN df_old old ON {join_condition}
    WHERE NOT ({compare_condition})
    """
    
    deletes_sql = f"""
    SELECT old.*, 'Delete' as Change_Type, '{new_name}' as New_DF, '{old_name}' as Old_DF
    FROM df_old old
    LEFT JOIN df_new new ON {join_condition}
    WHERE new.{join_keys[0]} IS NULL
    """
    
    # Execute queries
    df_inserts = spark.sql(inserts_sql)
    df_updates = spark.sql(updates_sql)
    df_deletes = spark.sql(deletes_sql)
    
    # Union all changes
    df_changes = df_inserts.union(df_updates).union(df_deletes)
    
    return df_changes

def summarize_cdc_changes(df_changes: DataFrame) -> DataFrame:
    # Count the number of changes for each type along with DataFrame names
    change_summary = df_changes.groupBy("Change_Type", "Old_DF", "New_DF").count()
    
    return change_summary

# Example usage with DataFrame names
old_name = 'df_old_snapshot'
new_name = 'df_new_snapshot'
join_keys = ['id']
compare_columns = ['name', 'age', 'salary']
df_changes = perform_cdc(df_old, df_new, join_keys, compare_columns, old_name, new_name)
df_changes_summary = summarize_cdc_changes(df_changes)


# In[5]:


df_changes.show()


# In[6]:


df_changes_summary.show()


# In[ ]:




