GCP config options 

# HOW TO TO CREATE A SELF-MANAGED INSTANCE
1. Go to console.cloud.google.com/sql/instances/
2. Click create instance
3. Choose MySQL
    MYsql Settings: enterprise
    Editional preset: sandbox- shared core, 2cCPU/8 GBRAM 
    Instance ID: omelet
    Password: R!ce1234
    Region : US-East4 (Northern Virginia) - Single zone

ETA for uploading database was 5 minutes
4. Adding Connections
    Choose database engine then click connections 
    Select Networking
    Select public IP with 0.0.0.0/0
    Add network 0.0.0.0/0
    * you may see a pop up fro no authorized external connections to cloud SQL instance and a disclosure that you are opening instance to all IPv4 CLients
Connect MySQL with Python Framework 

ETA for uploading database was 5 minutes



```bash
# If using a notebook...use the ! , if not, remove the ! in front of the commands
!sudo apt-get install python3-dev default-libmysqlclient-dev
!pip install pymysq
```
```bash
from sqlalchemy import create_engine 
```
```bash
MYSQL_HOSTNAME = ‘INSERT_HERE'
MYSQL_USER = ‘INSERT_HERE'
MYSQL_PASSWORD = 'INSERT_HERE'
MYSQL_DATABASE = ‘INSERT_HERE'
```
```bash
connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'
db = create_engine(connection_string)
```
To connect mysql with python 
```bash
import pandas as pd
```
```bash
query = """SELECT * FROM patient limit 10;""".format(MYSQL_DATABASE)
events_df = pd.read_sql(query, con=db)
events_df
```