# Pandasql Module - Query Pandas DataFrames using SQL syntax 
# pandasql uses SQLite syntax. Any pandas dataframes will be automatically detected by pandasql.
# You can query them as you would any regular SQL table
# pip install pandasql - https://pypi.org/project/pandasql/

import imp
import pandas as pd
import pandasql as ps

# Read Excel files to Pandas dataframe objects using Pandas
df = pd.read_excel(r"C:\Users\lohith\Desktop\SampleSuperstore.xlsx")

# Query Pandas DataFrames using pandasql Module
df1 =ps.sqldf("""
select * 
from df 
where Segment = 'Consumer' and 
Quantity = 2 and 
Discount = 0.0 and
Country = 'United States' and
[Ship Mode] = 'Second Class'
Limit 10
""")

print(df1)



