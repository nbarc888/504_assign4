empty bash: 

```bash

```

How to create cloud storage on google - 
504-database rec 1 2:00:00

1. Create a bucket - GCP
give it a name and add label optional
- choose where to store data: default is US , you can choose different regions. 
- add cross bucket which creates a replica with quiries and that whenever changes happen this gets added to secondary bucket
- you can do dual region optional
- how to store data: default storage standard,h iarchical name disabled, anywhere chashe disabled. 
- use syandard !!!
- choose how to control access to objects: pubnlic access prevention "ON" , access control : uniform 
- choose how to protect object data : soft delete policy: default, object versioning: disabled, bucklet retention policyL disabled, object retention: Disabled, encryption type: google managed. 
- if you click on choose how to protect object data you can toggle options
- note if you choose object versioning max number of vbersions per object 10 and expire noncurrent versions after 5 days.
- data encrption - defualt 
- create bucket 
- note: for class enforce piblic access prevention on bucket was clicked off just for class example. for creation you keep it. 
2. you get into bucket cloud storage, create folter then inside folder you can click into it and then upload lifes. example to upload is clinical data in github folder. then upload files into upload. they are sharable. 
- if you need to update files or updated something within the file, upload the same file then resolve object conflict pop ups, you can opt to overwrite the object or exclude object from this upload. 
- you can see version history and can update file and also vew previous versions, file name can stay the same and object changes. 
- to access and check public url you go to buckets tab and click and copy public url in middle (note it is lcoked by default)
- to get to full folder click the middle name of the folder , go to configuration and then edit access control 
- to manage access you can click or select the bucket and then scroll to access control and then toggle prevent public access to this bucket
- note gsirl URI is for google specific package as a shortcut
- note google also has made it significantly harder to turn on public access after disabling it. 

How to create cloud storage on Azure 2:20:20
1. go to all services and then storage accounts
- hit create 
- insert storage account name and select region 
- preferred storage type : azure blob storage , Standard performance and redundancy as geo-redundant storage. 
- go to advanced, disable reqire transfer for Rest api and disable enable storage account key access. only enable storage access if you want to enable or create a token. 
- review and create and then wait for deployment. 
- open and explore to get metadata nd monitoring recomendations
click open and explore, go to storage browser and you can see mult storage options, then go to blob containers, click upload and create container 
(class example patient stuff is name), then under folder/container then you can upload blob and folders and then change access level 
data sharing is easier in azure 
- note: permissions are based on org
- then go to overview and copy paste url. it may not work directrly 
- go to generate SAS to generate a key 
    go to account key and click generate sas token and url, the token key is sharable : seen on teams azure link file.
- to add argue ments its seen on the url after data.csv it is tehe "?sp="then random letters. the latter halfis the secret part "spr" see 2:30:00 for clarification. 
- also keep in mind keys can expire and are set to expire. 
______________________________________________________________


Recording 2: DB part 1

note: refer to slides for DBs in cloud 

refer to slide 50 
GCP config options 
- create my sql. enterprise, sandbox, shared core, 1cCPU/.614 gbRAM 
- go to console.cloud.google.com/sql/instances/
= choose database engine then click connections and select public IP with 0.0.0.0/0
- add network 0.0.0.0/0
Connect MySQL with Python Framework 
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
_______________________________________________________________

Recording 3: DB part 2 

00:45:00 - let of at 00:46:00

refer to slides to get proper list of commands to insert in terminal 
leaves off on slide 56 - how to create one on Azure
go to virtual machines, add virual machine 
- select region, ubuntu, standard with 8gb memory, standard_b1ls loading prince 
- insert username, password and confirm passwork
- enable all inbound port rules and selevy inbpount ports HTTP80, HTTPS443 and SSH22
- ease virtual machine: OS disk tupe standard HDD, and default encryption


to update ubuntu OS server
```bash
sudo apt-get update
```
to install mysql
```bash
sudo apt install mysql-server mysql-client
```
to log in 
```bash
sudo mysql
```
doing basic commands
```bash
show databases;
```
### create new user -dba- for us to connect with
step 1 - create user  'hants'@'%' IDENTIFIED BY 'hants2023';
THEN CONFIRM: 
```bash
select user from mysql.user;
```
step 2 - grant all priviledges on *.* to 'dba'@'%' WITH GRANT
OPTION;
THEN CONFIRM: show grants for dba;

Test local user connection DBA
```bash
mysql -u dba -p 
```
logged in with dba - lets create a DB
```bash 
create database tempdata;
```
```bash
show databases;
```

TO CONNECT mysql with google colab using python framework 
```bash 
!sudo apt-get install python3-dev default-libmysqlclient-dev
!pip install pymysql
from sqlalchemy import create_engine
MYSQL_HOSTNAME = ‘INSERT_HERE' # you probably don't need to change this
MYSQL_USER = ‘INSERT_HERE'
MYSQL_PASSWORD = 'INSERT_HERE'
MYSQL_DATABASE = ‘INSERT_HERE'
connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'
db = create_engine(connection_string)
```
To connect mysql with google colab 
```bash
import pandas as pd
query = """SELECT * FROM patient limit 10;""".format(MYSQL_DATABASE)
events_df = pd.read_sql(query, con=db)
events_df
```
____________ 0:55:00
### To create a DB with GCP create a VM as usual but with these specs: 
E2, Small shared Core-2GB, OS-Ubuntu 10GB   
For networking : Allow all HTTP and HTTPS but in example we'd do it seperately and not in the direct creation. If none allowed there's timeout errors due to unable to connect. 
Then hit create 

____________ 00:59:00

You are gonna need extrernal IP to the right side 

then you check firewall rules to change rules, search firewall, then create firewall rule to add port for project. 

name : mysql
targets: specified 
target tag: all instances
source: 0.0.0.0./0
enable tcp 3306
everything else is default

then create 

Note: 
Default SSH is 22. Other ports are off by default for security purposes.  

launch SHH in browser tp Launch terminal 1:15:00

#### Within terminal add in these commands

Update ubuntu
```bash
sudo apt-get update
```
To install mysql
```bash
sudo apt install mysql-server mysql-client #-y (if you add this arguement it autosays yes which is optional)
```
To log in - this 
```bash
sudo mysql
```
*** note in recording following response occurred " I'm afriaid I can't do that"
```bash
mysql
```
*** access denied for user 
Skip to 1:25:00
###### Exit out of SHH browser then input following commands
```Bash 
sudo apt install nano
```
then
```bash
sudo mysql
```
Then terminal goes into sql mode shown as below
```
mysql>
```
To connect to another database
```bash
mysql -u hants -h 34.23.52.32 -p
```
note: u stands for user, h stands for host
logs out then back in shh
```bash
sudo mysql
```
then it works 

### Doing basic commands
To show databases: 
```bash
show databases;
```
To create database
```bash 
create database hants;
```
*** output: query ok 1 row affected 0.01sec
To show table of a database 
```bash 
use hants;
```
```bash
show tables;
```
#####  new user -dba- for us to connect with
step 1 -
```bash
create user  'hants'@'34.23.53.13';  IDENTIFIED BY 'hants2025';
# hants is the dba name you can swap it to a different db
# above numbers are the ip address
```
if you put in following command
```bash
create user # literally anything
```
you just get a bunch of lines ->
but when you enter 
```
;
```
it completes the query but creates a user with no passcode
To exit the line 
```bash 
ctrl+C or \c
```
```bash
create user 'dba'@'%' identified by 'dba2025';
### dba2-25 section is the password
```
THEN CONFIRM by selecting user: 
```bash
select * from mysql.user;
```
*** you do get text back but its all lines and column names

To properly get a organized table of the user and permissions 
```bash
select * from mysql.user \G;
```
to select host user 
```bash
select Host, User from mysql.user;
```
_____
step 2 - 

```bash 
grant all priviledges on *.* to 'dba'@'%' WITH GRANT
OPTION;
#*.* means all data bases and all tables or can be swapped with a specific database
# dba can be swapped with the user  
# % means everywhere/regardless of ip 
```
example: 
```bash
grant all privileges on hants.ideas to 'dba'@'%'
### this only grants permissions on the ideas table within the hants database
```
command used in class
```bash 
grant all privileges on *.* to 'dba'@'%' with grant option;
```
*** query ok 
to recheck priviledges 
```bash 
select * from mysql.user where user like 'dba' \G
```
### you need to go into the configuration file and find the bind address see slide 101
find on "bind-address" = numbers 

what you now need to do is bind the external IP address to the mysql server , see slide 101 
then change bind address to 0.0.0.0 which tells it to take whatever the default ip is nd make it the entry point.

relaunch SHH 

```bash 
sudo apt install nano 
```
then to go to configuration file : /etc/mysql/mysql.conf.d/mysqld.cnf see slide 99

```bash
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
# replace that with config file path
```
THIS THEN TAKES YOU A MENU WHICH YOU NEED TO USE ARROW KEYS TO NAVIGATE!!!!!
change bind address by going to bind-address and then delete the numbers and change to 0.0.0.0
change the mysqlx-bind-address as well = 0.0.0.0

#### To save hit 'Ctrl'+'O' and then CTRL + X to exit
01:57:50

For changes to take place inorder to restart mysql
```bash
sudo systemctl mysql restart
```
2:00:00 

THEN CONFIRM: show grants for dba;

Test local user connection DBA
```bash
mysql -u dba -p 
```
*** note when input without the p it did not work

to log in 
```bash
mysql -u dba -h 35.333.333.333 -p
### replace above with actual ip addres of user.host
### password: dba2025
```
this will then proompt a password and then when you hit enter it enables it

### note USE GOOGLE SHELL FOR TESTING and insurt upper commands

2:08:00 shows observability 
more managed route you can launch it at an additional cost 

2:30:00 shows Azure route 