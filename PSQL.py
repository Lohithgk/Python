import imp
import pandas as pd
import pandasql as ps


df = pd.read_excel(r"C:\Users\klohith\OneDrive - LKQ\Desktop\SampleSuperstore.xlsx")

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



