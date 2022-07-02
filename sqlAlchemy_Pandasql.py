
import pandas as pd
import pandasql as ps
from sqlalchemy.engine import URL
from sqlalchemy import create_engine


connection_string = "DRIVER={SQL Server};SERVER=LOHITHGK;DATABASE=AdWorks"
connection_url = URL.create(
    "mssql+pyodbc", query={"odbc_connect": connection_string})

conn = create_engine(connection_url)

sql_query = pd.read_sql_query(
    sql='SELECT * FROM [AdWorks].[Person].[BusinessEntityContact]', con=conn)

# Convert SQL to DataFrame
BusinessEntityContact = pd.DataFrame(sql_query)

df = ps.sqldf(
    """
    SELECT
    BusinessEntityID, 
    PersonID, 
    ContactTypeID
    FROM BusinessEntityContact 
    limit 2    
    """
)

print(df)

conn.dispose()
