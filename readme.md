ignore sql scripts until further notice for now 11/3

goal is to use one cloud source. Goal: use google cloud if possible 

Assignment link: https://github.com/hantswilliams/HHA-504-2025/blob/main/assignment_4/database_deployment.md

You will provision two MySQL databases on the same cloud: (A) a VM you harden and configure yourself, and (B) the cloud’s managed MySQL offering. You will then connect to both using SQLAlchemy in Python, create a new database and table with pandas, insert data, and read it back. You will document steps, timing, and the differences in setup effort and operational friction.

Managed service names by cloud

Azure: Azure Database for MySQL – Flexible Server
GCP: Cloud SQL for MySQL
OCI: MySQL Database Service (MDS)

VM services by cloud

Azure: Azure Virtual Machines
GCP: Compute Engine
OCI: Compute

###  Repository & Deliverables

Create a repo named **`HHA504_mysql_vm_vs_managed`** with this structure:

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