
Assignment link: https://github.com/hantswilliams/HHA-504-2025/blob/main/assignment_4/database_deployment.md


### Videos
Managed DB: https://youtu.be/LJhiQ5PFzwU 


VM: https://www.youtube.com/watch?v=g5sBPRp9DPY

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


-----

##### virtualmachine.py
```bash
scripts/virtualmachine.py
```

##### managed_service.py
```bash
scripts/managed_service.py
```


### Steps used for connection in cloud shell 

Update ubuntu 
```bash
sudo apt-get update
```

To install nano
```Bash 
sudo apt install nano
```

To install mysql
```bash
sudo apt install mysql-server mysql-client #-y 
# (if you add this arguement it autosays yes which is optional)
```

To connect to sql database 
```bash
sudo mysql
```

To connect to another database seen in managed database
```bash
mysql -u #username -h #ipaddressnumbers -p
```

note: u stands for user, h stands for host
##### Exit out of SHH then back in SHH
```bash
sudo mysql
```




### Screenshot and summaries 
please see code for quick descriptions of each screenshot


##### Managed Screenshots

![Screenshot of two instances created, both had the same specs however i created two, one for the purpose of deletion](screenshots/managed/instance1.PNG)  
![Screenshot of the same two instances but both are now online](screenshots/managed/instance2.PNG)
![Screenshot of showing how and where to delete the instance](screenshots/managed/instancedelete.PNG)
![Screenshot of omelet instance networking](screenshots/managed/sm2.JPG)
![Screenshot of username and password for sql database. Google managed has the ability to create usernames without having to enter the cloudshell terminal](screenshots/managed/usercreate.PNG)
![Screenshot of list of databases on Managed cloud sql menu](screenshots/managed/newdatabaseviamenu.PNG)
![Google cloud has the ability to make queries directly though its menu instead of cloudshell](screenshots/managed/querytableverify.PNG)
![Cloudshell connection](screenshots/managed/cloudshellconnect.PNG)
![Cloudshell databases shown](screenshots/managed/cloudshell.PNG)


##### VM Screenshots 

![Vm instance created for this assignment](screenshots/vm/vm1.PNG)
![Databases within VM instance](screenshots/vm/vm2.PNG)
![Screenshot of nano package installation along with sudo mysql command being used](screenshots/vm/mysqlnanoinstall.PNG)
![Screenshot of nano and change of bind-address and mysqlx-bind-address](screenshots/vm/nanobind.PNG)
![Creation of user salmon and granting permissions for user salmon. please note \G is used to organize the output](screenshots/vm/usercreate.PNG)
![User permissions of user salmon showing that user has access and permissions similar to admin permissions](screenshots/vm/userperm.PNG)
![Screenshot showing connection using salmon and showing databases present within sql instance](screenshots/vm/databasesushi.PNG)
![Screenshot showing both commands and output which includes table of vitals within vitals database](screenshots/vm/dbconfirmtable.PNG)
![Connection using cloudshell terminal rather than shh](screenshots/vm/successfulconnectioncloudshell.PNG)
![Using cloudshell to show databases within instance](screenshots/vm/cloudshelldatabase.PNG)
![Screenshot of VM instance  obervability page](screenshots/vm/observability.PNG)

