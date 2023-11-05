import duckdb as dd
import polars as pl

df = pl.read_csv(
    source= 'C:\\Users\\klohith\\Desktop\\viewPointsTableExcel.csv', has_header= True)

dd.sql(
    """
    select * 
    from df
    where df.TEAM == 'India' """   
).show()

df1 = dd.read_csv('C:\\Users\\klohith\\Desktop\\viewPointsTableExcel.csv', header=True)

dd.sql(
    """
    select * 
    from df1
    where df1.TEAM in ('India', 'New Zealand')
"""
).show()

