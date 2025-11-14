# HOW TO TO CREATE A MANAGED INSTANCE
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
    * you may see a pop up from no authorized external connections to cloud SQL instance and a disclosure that you are opening instance to all IPv4 CLients
Connect MySQL with Python Framework 

5. To create a new database via the menu go to databases, create database and enter fields: 
    database name: egg
    character set utf8mb4
    default collection

6. Open CloudSql Studio
    a. This will prompt you to log into database and create a new user
        Create a new user and password
    b. Go back to CloudSql Studio and log in with new user
        Go to Explorer tab on lefthand side and click on following items: 
1. Tables 
    create a new query
    insert following code from managed_service.py 
```bash
            CREATE TABLE patient_vitals (
            patient_id INT NOT NULL,
            visit_date DATE NOT NULL,
            bp_sys INT,
            bp_dia INT,
            hr INT,
            PRIMARY KEY (patient_id, visit_date)
            );
```
to insert data into the new table create another query and insert following code: 

```bash
            INSERT INTO patient_vitals (patient_id, visit_date, bp_sys, bp_dia, hr)
            VALUES
                (1, '2025-09-01', 118, 76, 72),
                (2, '2025-09-02', 78, 35, 130),
                (3, '2025-09-03', 121, 79, 95); 
```

2. Testing the query table
    create a new query to show whole table
```bash
            SELECT * FROM patient_vitals;
``` 

-------------
```bash
mysql -u chef -h 34.85.160.89 -p
```

then proceed to enter password

```bash
show databases;
```

to create database
```bash
create database cookbook;
```

then use the new database
```bash
use cookbook;
```

to insert new table into the cookbook 
```bash
create table page1
```

checking database to confirm creation
```bash
show databases
```



