# How to Create a VM managed Database

#### Region: US-East1 (SC) 

- insert username, password and confirm password
- enable all inbound port rules and selevy inbpount ports HTTP80, HTTPS443 and SSH22
- ease virtual machine: OS disk tupe standard HDD, and default encryption


##### VM specs: 
Machine Type: E2 Series
Size : e2-Small shared Core - 2 GB memory
Operating System: Ubuntu - Version: 25.10 minimal  10 GB size
For networking : Allow all HTTP and HTTPS
##### networking and port rules
allow all HTTP and HTTPS
#### network keys 


##### Firewall additional add-on
name : mysql
target tag: all instances
source IPv4: 0.0.0.0./0
enable tcp 3306

Name of VM instance: salmon 
Internal IP: 10.150.0.4
old External IP: 34.48.227.25

New External IP: 35.231.55.63



## SHH commands and directions
to update ubuntu OS server
```bash
sudo apt-get update
```
to install mysql
```bash
sudo apt install mysql-server 
```
```bash
sudo apt install mysql-client
```

to log in 
```bash
sudo mysql
```
Note: If command does not work what you can do is exit out of shh and come back in again



doing basic commands
```bash
show databases;
```


to create a new user
salmon is username
salmon123 is password

```bash 
create user  'salmon'@'%' IDENTIFIED BY 'salmon123';
```

to verify user creation 
```bash 
select user from mysql.user;
```

to grant admin or all permissions
```bash 
grant all priviledges on *.* to 'salmon'@'%' WITH GRANT OPTION;
#*.* means all data bases and all tables or can be swapped with a specific database
# dba can be swapped with the user  
# % means everywhere/regardless of ip 
```


to show permissions
```bash
select * from mysql.user where user like 'salmon' \G
```


to exit out of sql
```bash
exit
```

###### Exit out of SHH browser then input following commands


```Bash 
sudo apt install nano
```

```bash 
sudo mysql
```

to create data base
```bash
create database sushi;
```

to use database
```bash
use sushi;
```
```bash 
show tables; ### should show and empty table
```

to enter a non-empty database 
```bash
use vitals
```

to show list of tables
```bash
show tables; 
```

to show table contents
```bash
SELECT * FROM ED_vitals;
```


### To configure bind address

at this point you can either choose to exit mysql or relaunch SHH 

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


For changes to take place inorder to restart mysql (if command doesnt work exit shh)
```bash
sudo systemctl restart mysql
```

# Python code testing 

See virtualmachine.py in scripts
Run code section by section inorder to run properly! 
