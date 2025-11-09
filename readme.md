
goal is to use one cloud source. Goal: use google cloud

Assignment link: https://github.com/hantswilliams/HHA-504-2025/blob/main/assignment_4/database_deployment.md

You will provision two MySQL databases on the same cloud: (A) a VM you harden and configure yourself, and (B) the cloud’s managed MySQL offering. You will then connect to both using SQLAlchemy in Python, create a new database and table with pandas, insert data, and read it back. You will document steps, timing, and the differences in setup effort and operational friction.

### Videos
Self-Managed DB: https://youtu.be/LJhiQ5PFzwU 


Managed service names by cloud
- GCP: Cloud SQL for MySQL

VM services by cloud
- GCP: Compute Engine


## Cloud selected: GCP
#### Region: US-East1 (SC) 
##### VM specs: 
Machine Type: E2 Series
Size : e2-Small shared Core - 2 GB memory
Operating System: Ubuntu - Version: 25.10 minimal  10 GB size
For networking : Allow all HTTP and HTTPS
##### Firewall additional add-on
name : mysql
targets: specified 
target tag: all instances
source: 0.0.0.0./0
enable tcp 3306


###  Database Specs: 




### Scripts to copy 


scripts/vm_demo.py
```bash

```

scripts/managed_demo.py
```bash

```


### Steps to reproduce 

Update ubuntu
```bash
sudo apt-get update
```
```Bash 
sudo apt install nano
```
To install mysql
```bash
sudo apt install mysql-server mysql-client #-y 
# (if you add this arguement it autosays yes which is optional)
```
To log in - this 
```bash
sudo mysql
```
To connect to another database
```bash
mysql -u hants -h 34.23.52.32 -p
```
note: u stands for user, h stands for host
##### Exit out of SHH then back in SHH
```bash
sudo mysql
```
then it works 

Commands for Query: 
```bash

```
```bash

```
```bash
SHOW DATABASES;
```


















structure:

```
HHA504_mysql_vm_vs_managed/
├─ README.md
├─ .gitignore                  # Make sure to ignore your .env 
├─ .env.example                # Do NOT commit real secrets
├─ scripts/
│   ├─ vm_demo.py              # SQLAlchemy+pandas against VM MySQL
│   └─ managed_demo.py         # SQLAlchemy+pandas against managed MySQL
├─ sql/
│   └─ init.sql                # Optional: user/db bootstrap you ran on VM
├─ screenshots/
│   ├─ vm/                     # VM portal, firewall, daemon status, CLI, etc.
│   └─ managed/                # Managed service creation, connection details
└─ docs/
    ├─ setup_notes_vm.md
    ├─ setup_notes_managed.md
    └─ comparison.md           # timing & difficulty comparison
```