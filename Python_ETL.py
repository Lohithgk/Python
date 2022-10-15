
# Import Required Modules
import pandas as pd
import glob
import gc
from datetime import date, timedelta
import warnings
from sqlalchemy.engine import URL
from sqlalchemy import create_engine

# get the today's date from the Date module, and pass it as variable d1 to file location path
Today = date.today() - timedelta(days=0)
Todays_Date = Today.strftime("%Y-%m-%d")

# get the today's WAL9110 file available in the network path and Store the file's Object Name in files
files = glob.glob(
    f'K:\KAS100 Data Files\Sales_Person\Data_Exports\WAL9110_SalesPerson\*\{Todays_Date}-*.xlsx')

# If Today's SAL8110 file is available in the network path then Load it to WAL9110 Dataframe
if files:
    for excel_file in files:

        # Ignore warnings, and load the data in the Today Excel file's to a WAL9110 Dataframe.
        warnings.simplefilter("ignore")
        WAL9110 = pd.read_excel(excel_file, na_values=[
                                '0001-00-01 12:00:00.000'])

        # Create the connection to Microsoft SQL SERVER
        connection_string = """DRIVER={ODBC Driver 13 for SQL Server}; 
                               SERVER=Lohithgk; 
                               DATABASE=AdventureWorks; 
                               Trusted_Connection=yes"""
        connection_url = URL.create(
            "mssql+pyodbc", query={"odbc_connect": connection_string})
        connection = create_engine(connection_url)

        # Overwrite the data in the dataframe to SQL Table [AdventureWorks].[dbo].[SalesPerson]
        WAL9110.to_sql(name='SalesPerson', con=connection, schema='dbo',
                       index=False, if_exists='replace')

        # Close the Microsoft SQL SERVER Connection
        connection.dispose()

        # Delete the WAL9110 Dataframe and Clear the garbage collected in the RAM
        del WAL9110
        gc.collect()

else:
    print("Today's WAL9110 is not available in the network Path")
